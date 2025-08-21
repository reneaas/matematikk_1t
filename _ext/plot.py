"""plot directive: generate and inline a function plot using plotmath.

Features:
 - Expression compiled safely with sympy -> numpy (vectorized)
 - Caching via hashed parameters unless :nocache: set
 - Optional :debug: flag preserves original SVG (no stripping / id rewrite) and also saves PDF copy
 - Width control (percent or fixed) and unique ID rewriting (safe) for multiple instances on same page
 - YAML front matter (--- ... ---) or simple key: value lines before caption

Usage examples (in .md / .rst):

.. plot::
   :fn: sin(x)/x
   :fn_label: f(x) = sin(x)/x
   :xmin: -10
   :xmax: 10
   :ymin: -0.5
   :ymax: 1.2
   :grid:
   :ticks:
   :width: 70%

Caption text here (optional).

Or with content block (YAML style):

.. plot::

   ---
   fn: sin(x)/x
   fn_label: f(x) = sin(x)/x
   xmin: -10
   xmax: 10
   ---
   En beskrivende bildetekst.
"""

from __future__ import annotations

import os
import re
import uuid
import hashlib
import shutil
from typing import Callable, Dict, Any, Tuple

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
class PlotDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    option_spec = {
        "fn": directives.unchanged_required,
        "fn_label": directives.unchanged,
        "xmin": directives.unchanged,
        "xmax": directives.unchanged,
        "ymin": directives.unchanged,
        "ymax": directives.unchanged,
        "xstep": directives.unchanged,
        "ystep": directives.unchanged,
        "fontsize": directives.unchanged,
        "lw": directives.unchanged,
        "alpha": directives.unchanged,
        "domain": directives.unchanged,  # reserved for future shading
        "grid": directives.flag,
        "ticks": directives.flag,
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
        if "fn" not in merged:
            return [
                self.state_machine.reporter.error(
                    "Directive 'plot' krever 'fn:'", line=self.lineno
                )
            ]

        expr = merged["fn"].strip()
        try:
            fn_callable = _compile_function(expr)
        except Exception as e:
            return [self.state_machine.reporter.error(str(e), line=self.lineno)]

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
        try:
            alpha = float(alpha_raw) if alpha_raw not in (None, "") else None
        except Exception:
            alpha = None
        domain_str = merged.get("domain", "").strip()

        grid_flag = ("grid" in merged) or (
            "grid" not in merged and "ticks" not in merged
        )
        ticks_flag = ("ticks" in merged) or (
            "grid" not in merged and "ticks" not in merged
        )

        label_raw = merged.get("fn_label", "").strip()
        labels_arg = [label_raw] if label_raw else True
        explicit_name = merged.get("name")
        debug_mode = "debug" in merged

        content_hash = _hash_key(
            expr,
            label_raw,
            xmin,
            xmax,
            ymin,
            ymax,
            xstep,
            ystep,
            fontsize,
            lw,
            alpha,
            domain_str,
            int(grid_flag),
            int(ticks_flag),
        )
        base_name = explicit_name or f"plot_{content_hash}"

        rel_dir = os.path.join("_static", "plot")
        abs_dir = os.path.join(app.srcdir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)
        svg_name = f"{base_name}.svg"
        abs_svg = os.path.join(abs_dir, svg_name)

        regenerate = ("nocache" in merged) or not os.path.exists(abs_svg)
        if regenerate:
            import matplotlib

            matplotlib.use("Agg")  # headless
            try:
                fig, ax = plotmath.plot(
                    functions=[fn_callable],
                    fn_labels=labels_arg,
                    xmin=xmin,
                    xmax=xmax,
                    ymin=ymin,
                    ymax=ymax,
                    ticks=ticks_flag,
                    xstep=xstep,
                    ystep=ystep,
                    grid=grid_flag,
                    lw=lw,
                    alpha=alpha,
                    domain=False,
                    fontsize=fontsize,
                    figsize=None,
                )
                fig.savefig(
                    abs_svg, format="svg", bbox_inches="tight", transparent=True
                )
                # try:
                #     fig.savefig(
                #         os.path.splitext(abs_svg)[0] + ".pdf",
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
                    "plot: SVG mangler.", line=self.lineno
                )
            ]

            # Remove width/height for responsiveness unless debug
            # Only strip width/height on the ROOT <svg> tag (keep clipPath sizes)
            def _strip_root_svg_size(svg_text: str) -> str:
                def repl(m):
                    tag = m.group(0)
                    tag = re.sub(r'\swidth="[^"]+"', "", tag)
                    tag = re.sub(r'\sheight="[^"]+"', "", tag)
                    return tag

                return re.sub(r"<svg\b[^>]*>", repl, svg_text, count=1)

            if not debug_mode and "viewBox" in raw_svg:
                raw_svg = _strip_root_svg_size(raw_svg)

        env.note_dependency(abs_svg)
        try:  # copy to output _static
            out_static = os.path.join(app.outdir, "_static", "plot")
            os.makedirs(out_static, exist_ok=True)
            shutil.copy2(abs_svg, os.path.join(out_static, svg_name))
        except Exception:
            pass

        try:
            raw_svg = open(abs_svg, "r", encoding="utf-8").read()
        except Exception as e:
            return [
                self.state_machine.reporter.error(
                    f"plot inline: kunne ikke lese SVG: {e}", line=self.lineno
                )
            ]

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
                raw_svg, f"gr_{content_hash}_{uuid.uuid4().hex[:6]}_"
            )

        alt_default = f"Graf av f(x) = {expr}"
        if domain_str:
            alt_default += f" for {domain_str}"
        alt = merged.get("alt", alt_default)

        width_opt = merged.get("width")
        percent = isinstance(width_opt, str) and width_opt.strip().endswith("%")

        def _augment(m):
            tag = m.group(0)
            if "class=" not in tag:
                tag = tag[:-1] + ' class="plot-inline-svg"' + ">"
            else:
                tag = tag.replace('class="', 'class="plot-inline-svg ')
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
            ["adaptive-figure", "plot-figure", "no-click"]
        )
        raw_node = nodes.raw("", raw_svg, format="html")
        raw_node.setdefault("classes", []).extend(
            ["plot-image", "no-click", "no-scaled-link"]
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
    app.add_directive("plot", PlotDirective)
    return {"version": "0.2", "parallel_read_safe": True, "parallel_write_safe": True}
