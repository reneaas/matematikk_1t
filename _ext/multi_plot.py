"""multi-plot directive: create a grid of function plots using plotmath.multiplot.

Features:
 - Accepts a list of function expressions and plots each in a grid (rows x cols)
 - Expressions compiled safely with sympy -> numpy (vectorized)
 - Caching via hashed parameters unless :nocache: set
 - Optional :debug: preserves original SVG (no stripping / id rewrite) and also saves PDF copy
 - Width control and safe ID rewriting for multiple instances on same page
 - YAML front matter (--- ... ---) or simple key: value lines before caption

Usage (MyST):

:::{multi-plot}
---
functions: [x**2 - 2*x, -x + 2, x - 3]
rows: 1
cols: 3
width: 100%
---
:::
"""

from __future__ import annotations

import os
import re
import uuid
import hashlib
import shutil
from typing import Callable, Dict, Any, Tuple, List

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _hash_key(*parts) -> str:
    h = hashlib.sha1()
    for p in parts:
        if p is None:
            p = "__NONE__"
        h.update(str(p).encode("utf-8"))
        h.update(b"||")
    return h.hexdigest()[:12]


def _compile_function(expr: str) -> Callable:
    import sympy, numpy as np  # local import

    expr = expr.strip()
    x = sympy.symbols("x")
    try:
        sym = sympy.sympify(expr)
    except Exception as e:  # pragma: no cover - user error path
        raise ValueError(f"Ugyldig funksjonsuttrykk '{expr}': {e}")
    fn_np = sympy.lambdify(x, sym, modules=["numpy"])

    def f(arr):
        return fn_np(np.asarray(arr, dtype=float))

    # simple vectorization test
    _ = f([0.0, 1.0])
    return f


# ---------------------------------------------------------------------------
# Directive
# ---------------------------------------------------------------------------


def _strip_root_svg_size(svg_text: str) -> str:
    """Remove width/height only on the root <svg> tag for responsiveness."""

    def repl(m):
        tag = m.group(0)
        tag = re.sub(r'\swidth="[^"]+"', "", tag)
        tag = re.sub(r'\sheight="[^"]+"', "", tag)
        return tag

    return re.sub(r"<svg\b[^>]*>", repl, svg_text, count=1)


def _parse_bool(val, default: bool | None = None) -> bool | None:
    if val is None:
        return default
    if isinstance(val, bool):
        return val
    s = str(val).strip().lower()
    if s == "":  # option present with no value => treat as True
        return True
    if s in {"true", "yes", "on", "1"}:
        return True
    if s in {"false", "no", "off", "0"}:
        return False
    return default


def _split_expr_list(val: str) -> List[str]:
    if not isinstance(val, str):
        return []
    s = val.strip()
    if not s:
        return []
    # allow [a,b,c] or a;b;c or a,b,c
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    s = s.replace(";", ",")
    parts = [p.strip() for p in s.split(",")]
    return [p for p in parts if p]


class MultiPlotDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    option_spec = {
        "functions": directives.unchanged_required,  # list of expressions
        "fn_labels": directives.unchanged,  # optional list of labels
        "xmin": directives.unchanged,
        "xmax": directives.unchanged,
        "ymin": directives.unchanged,
        "ymax": directives.unchanged,
        "xstep": directives.unchanged,
        "ystep": directives.unchanged,
        "fontsize": directives.unchanged,
        "lw": directives.unchanged,
        "alpha": directives.unchanged,
        "grid": directives.unchanged,
        "ticks": directives.unchanged,
        "rows": directives.unchanged,
        "cols": directives.unchanged,
        "align": lambda a: directives.choice(a, ["left", "center", "right"]),
        "class": directives.class_option,
        "name": directives.unchanged,
        "nocache": directives.flag,
        "alt": directives.unchanged,
        "width": directives.length_or_percentage_or_unitless,
        "debug": directives.flag,
    }

    # -----------------------------
    # Content key/value parsing
    # -----------------------------
    def _gather_kv_from_content(self) -> Tuple[Dict[str, str], int]:
        kv: Dict[str, str] = {}
        lines = list(self.content)
        idx = 0
        # YAML front matter style
        if lines and lines[0].strip() == "---":
            idx = 1
            while idx < len(lines) and lines[idx].strip() != "---":
                line = lines[idx].rstrip()
                m = re.match(r"^([A-Za-z_][\w]*)\s*:\s*(.*)$", line)
                if m:
                    kv[m.group(1)] = m.group(2)
                idx += 1
            if idx < len(lines) and lines[idx].strip() == "---":
                idx += 1
            while idx < len(lines) and not lines[idx].strip():
                idx += 1
            return kv, idx
        # flat key: value lines until first non-matching or blank separation
        caption_start = 0
        for i, line in enumerate(lines):
            if not line.strip():
                caption_start = i + 1
                continue
            m = re.match(r"^([A-Za-z_][\w]*)\s*:\s*(.*)$", line)
            if m:
                kv[m.group(1)] = m.group(2)
                caption_start = i + 1
            else:
                break
        return kv, caption_start

    # -----------------------------
    # Main run
    # -----------------------------
    def run(self):  # noqa: C901 (complexity OK for directive)
        env = self.state.document.settings.env
        app = env.app
        try:
            import plotmath  # type: ignore
        except Exception as e:  # pragma: no cover - dependency missing
            err = nodes.error()
            err += nodes.paragraph(text=f"Kunne ikke importere plotmath: {e}")
            return [err]

        kv, caption_idx = self._gather_kv_from_content()
        merged: Dict[str, Any] = {**kv, **self.options}
        if "functions" not in merged:
            return [
                self.state_machine.reporter.error(
                    "Directive 'multi-plot' krever 'functions:'", line=self.lineno
                )
            ]

        exprs = _split_expr_list(str(merged["functions"]))
        if not exprs:
            return [
                self.state_machine.reporter.error(
                    "'functions' var tomt eller ugyldig.", line=self.lineno
                )
            ]
        # compile all
        functions: List[Callable] = []
        for e in exprs:
            try:
                functions.append(_compile_function(e))
            except Exception as ex:
                return [
                    self.state_machine.reporter.error(
                        f"Ugyldig funksjon '{e}': {ex}", line=self.lineno
                    )
                ]

        def _f(name, default):
            v = merged.get(name)
            if v in (None, ""):
                return default
            try:
                return float(v)
            except Exception:
                return default

        xmin = _f("xmin", -6)
        xmax = _f("xmax", 6)
        ymin = _f("ymin", -6)
        ymax = _f("ymax", 6)
        xstep = _f("xstep", 1)
        ystep = _f("ystep", 1)
        fontsize = _f("fontsize", 20)
        lw = _f("lw", 2.5)
        alpha_raw = merged.get("alpha")
        grid_flag = _parse_bool(merged.get("grid"), default=True)
        ticks_flag = _parse_bool(merged.get("ticks"), default=True)

        try:
            alpha = float(alpha_raw) if alpha_raw not in (None, "") else None
        except Exception:
            alpha = None

        labels_list: List[str] = _split_expr_list(str(merged.get("fn_labels", "")))
        if labels_list and len(labels_list) == len(functions):
            labels_arg: Any = labels_list
        else:
            labels_arg = True
        explicit_name = merged.get("name")
        debug_mode = "debug" in merged
        rows = int(float(merged.get("rows", 1)))
        cols = int(float(merged.get("cols", max(1, len(functions)))))

        content_hash = _hash_key(
            "|".join(exprs),
            "|".join(labels_list),
            xmin,
            xmax,
            ymin,
            ymax,
            xstep,
            ystep,
            fontsize,
            lw,
            alpha,
            rows,
            cols,
            int(grid_flag),
            int(ticks_flag),
        )
        base_name = explicit_name or f"multi_plot_{content_hash}"

        rel_dir = os.path.join("_static", "multi_plot")
        abs_dir = os.path.join(app.srcdir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        svg_name = f"{base_name}.svg"
        abs_svg = os.path.join(abs_dir, svg_name)

        regenerate = ("nocache" in merged) or not os.path.exists(abs_svg)
        if regenerate:
            try:
                letters = [chr(i) for i in range(65, 65 + len(functions))]
                fig, axes = plotmath.multiplot(
                    functions=functions,
                    fn_labels=letters,
                    xmin=xmin,
                    xmax=xmax,
                    ymin=ymin,
                    ymax=ymax,
                    xstep=xstep,
                    ystep=ystep,
                    ticks=ticks_flag,
                    grid=grid_flag,
                    rows=rows,
                    cols=cols,
                    lw=lw,
                    alpha=alpha,
                    fontsize=fontsize,
                    figsize=(4.5 * cols, 3.5 * rows),
                )
                # Save via the single Figure object
                fig.savefig(
                    abs_svg, format="svg", bbox_inches="tight", transparent=True
                )
                # Also save a PDF sidecar for debugging comparisons (optional)
                # try:
                #     fig.savefig(
                #         os.path.join(abs_dir, f"{base_name}.pdf"),
                #         format="pdf",
                #         bbox_inches="tight",
                #         transparent=True,
                #     )
                # except Exception:
                #     pass
            except Exception as e:
                return [
                    self.state_machine.reporter.error(
                        f"Feil under generering av graf: {e}", line=self.lineno
                    )
                ]

        if not os.path.exists(abs_svg):
            return [
                self.state_machine.reporter.error(
                    "multi-plot: SVG mangler.", line=self.lineno
                )
            ]

        env.note_dependency(abs_svg)
        try:  # copy to output _static
            out_static = os.path.join(app.outdir, "_static", "multi_plot")
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(abs_svg, os.path.join(out_static, svg_name))
        except Exception:
            pass

        try:
            raw_svg = open(abs_svg, "r", encoding="utf-8").read()
        except Exception as e:
            return [
                self.state_machine.reporter.error(
                    f"graph inline: kunne ikke lese SVG: {e}", line=self.lineno
                )
            ]

        if not debug_mode and "viewBox" in raw_svg:
            raw_svg = _strip_root_svg_size(raw_svg)

        def _rewrite_ids(txt: str, prefix: str) -> str:
            # Collect ids
            ids = re.findall(r'\bid="([^"]+)"', txt)
            if not ids:
                return txt
            # Skip font glyphs to avoid disrupting text rendering
            skip_prefixes = (
                "DejaVu",
                "CM",
                "STIX",
                "Nimbus",
                "Bitstream",
                "Arial",
                "Times",
                "Helvetica",
            )
            mapping = {}
            for i in ids:
                if i.startswith(skip_prefixes):
                    continue
                mapping[i] = f"{prefix}{i}"
            if not mapping:
                return txt

            # Replace id definitions
            def repl_id(m: re.Match) -> str:
                old = m.group(1)
                new = mapping.get(old, old)
                return f'id="{new}"'

            txt = re.sub(r'\bid="([^"]+)"', repl_id, txt)

            # Replace url(#id) everywhere (attributes and styles)
            def repl_url(m: re.Match) -> str:
                old = m.group(1).strip()
                new = mapping.get(old, old)
                return f"url(#{new})"

            txt = re.sub(r"url\(#\s*([^\)\s]+)\s*\)", repl_url, txt)

            # Replace href/xlink:href references supporting both quote styles
            def repl_href(m: re.Match) -> str:
                attr = m.group(1)
                quote = m.group(2)
                old = m.group(3).strip()
                new = mapping.get(old, old)
                return f"{attr}={quote}#{new}{quote}"

            txt = re.sub(
                r'(xlink:href|href)\s*=\s*(["\"])#\s*([^"\"]+)\s*\2',
                repl_href,
                txt,
            )
            return txt

        if not debug_mode:
            raw_svg = _rewrite_ids(
                raw_svg, f"mgr_{content_hash}_{uuid.uuid4().hex[:6]}_"
            )

        alt_default = f"Multiplot av {len(exprs)} funksjoner"
        alt = merged.get("alt", alt_default)

        width_opt = merged.get("width")
        percent = isinstance(width_opt, str) and width_opt.strip().endswith("%")

        def _augment(m):
            tag = m.group(0)
            if "class=" not in tag:
                tag = tag[:-1] + ' class="graph-inline-svg"' + ">"
            else:
                tag = tag.replace('class="', 'class="graph-inline-svg ')
            if alt and "aria-label=" not in tag:
                tag = tag[:-1] + f' role="img" aria-label="{alt}"' + ">"
            if width_opt:
                if percent:
                    wval = width_opt.strip()
                else:
                    wval = width_opt.strip()
                    if wval.isdigit():
                        wval += "px"
                style_frag = f"width:{wval}; height:auto; display:block; margin:0 auto;"
                if "style=" in tag:
                    tag = re.sub(
                        r'style="([^"]*)"',
                        lambda mm: f'style="{mm.group(1)}; {style_frag}"',
                        tag,
                        count=1,
                    )
                else:
                    tag = tag[:-1] + f' style="{style_frag}"' + ">"
            return tag

        raw_svg = re.sub(r"<svg\b[^>]*>", _augment, raw_svg, count=1)
        if alt and "<title" not in raw_svg:
            raw_svg = re.sub(
                r"(<svg\b[^>]*>)",
                r"\1<title>" + re.escape(alt) + r"</title>",
                raw_svg,
                count=1,
            )

        figure = nodes.figure()
        figure.setdefault("classes", []).extend(
            ["adaptive-figure", "multi-plot-figure", "no-click"]
        )
        raw_node = nodes.raw("", raw_svg, format="html")
        raw_node.setdefault("classes", []).extend(
            ["graph-image", "no-click", "no-scaled-link"]
        )
        figure += raw_node

        extra_classes = merged.get("class")
        if extra_classes:
            figure["classes"].extend(extra_classes)
        figure["align"] = merged.get("align", "center")

        caption_lines = list(self.content)[caption_idx:]
        while caption_lines and not caption_lines[0].strip():
            caption_lines.pop(0)
        if caption_lines:
            caption = nodes.caption()
            caption += nodes.Text("\n".join(caption_lines))
            figure += caption

        if explicit_name:
            self.add_name(figure)
        return [figure]


def setup(app):  # pragma: no cover
    app.add_directive("multi-plot", MultiPlotDirective)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
