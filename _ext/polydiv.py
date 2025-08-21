import os
import hashlib
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


def _hash_key(*parts):
    h = hashlib.sha1()
    for p in parts:
        if p is None:
            p = "__NONE__"
        h.update(str(p).encode("utf-8"))
        h.update(b"||")
    return h.hexdigest()[:12]


class PolyDivDirective(SphinxDirective):
    """Generate (and cache) a polynomial long division figure as SVG and embed it.

    Usage (MyST):

    ````
    ::::{polydiv}
    :p: x^3 + 2x^2 - 3x - 6
    :q: x - 2
    :stage: 2        # optional
    :vars: x         # optional (default x)
    :align: center   # optional (left|center|right)
    :class: small    # optional extra CSS classes on figure

    Valgfri bildetekst her.
    ::::
    ````

    Or classic reStructuredText:

    .. polydiv::
       :p: x^3 + 2x^2 - 3x - 6
       :q: x - 2
       :stage: 2
       :vars: x

       Valgfri bildetekst her.
    """

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "p": directives.unchanged_required,
        "q": directives.unchanged_required,
        "stage": directives.nonnegative_int,
        "vars": directives.unchanged,
        "align": lambda a: directives.choice(a, ["left", "center", "right"]),
        "class": directives.class_option,
        "name": directives.unchanged,  # optional explicit base filename / ref name
        "cache": directives.flag,  # include to enable (default on)
        "nocache": directives.flag,  # include to force regeneration
        "alt": directives.unchanged,
        "width": directives.length_or_percentage_or_unitless,
    }

    def run(self):
        env = self.state.document.settings.env

        try:
            from python_util.polydiv import polylongdiv
        except Exception as e:  # pragma: no cover
            msg = nodes.error()
            para = nodes.paragraph(text=f"Kunne ikke importere polydiv-modulen: {e}")
            msg += para
            return [msg]

        p = self.options.get("p")
        q = self.options.get("q")
        if p is None or q is None:
            error = self.state_machine.reporter.error(
                "Directive 'polydiv' krever både :p: og :q: opsjoner.",
                line=self.lineno,
            )
            return [error]

        stage = self.options.get("stage")
        vars_opt = self.options.get("vars", "x")

        explicit_name = self.options.get("name")
        content_hash = _hash_key(p, q, stage, vars_opt)
        base_name = explicit_name or f"polydiv_{content_hash}"

        # Directory for generated SVG (served as static file)
        src_dir = env.app.srcdir
        rel_dir = os.path.join("_static", "polydiv")
        abs_dir = os.path.join(src_dir, rel_dir)
        os.makedirs(abs_dir, exist_ok=True)

        svg_filename = f"{base_name}.svg"
        abs_svg_path = os.path.join(abs_dir, svg_filename)

        use_cache = "nocache" not in self.options
        regenerate = True
        if use_cache and os.path.exists(abs_svg_path):
            regenerate = False

        if regenerate:
            cwd = os.getcwd()
            try:
                os.chdir(abs_dir)
                polylongdiv(
                    fname=base_name,
                    p=p,
                    q=q,
                    stage=stage,
                    vars=vars_opt,
                )
            except Exception as e:  # pragma: no cover
                err = self.state_machine.reporter.error(
                    f"Feil under generering av polynomdivisjon: {e}",
                    line=self.lineno,
                )
                return [err]
            finally:
                os.chdir(cwd)

        # Post-process SVG: remove fixed width/height so it scales with CSS, keep viewBox
        try:
            if os.path.exists(abs_svg_path):
                with open(abs_svg_path, "r", encoding="utf-8") as f_svg:
                    svg_text = f_svg.read()
                # Only strip if a viewBox exists (so scaling remains defined)
                if "viewBox" in svg_text:
                    import re

                    cleaned = re.sub(r'\swidth="[^"]+"', "", svg_text)
                    cleaned = re.sub(r'\sheight="[^"]+"', "", cleaned)
                    if cleaned != svg_text:
                        with open(abs_svg_path, "w", encoding="utf-8") as f_svg:
                            f_svg.write(cleaned)
        except Exception:
            pass  # non-fatal

        uri = f"/{rel_dir}/{svg_filename}"
        if stage is not None:
            default_alt = f"Polynomdivisjon av ({p}) : ({q}) – trinn {stage}"
        else:
            default_alt = f"Polynomdivisjon av ({p}) : ({q})"
        alt = self.options.get("alt", default_alt)
        image_node = nodes.image(uri=uri, alt=alt)
        image_node.setdefault("classes", []).extend(["polydiv-image", "no-click"])
        width_opt = self.options.get("width")
        if width_opt:
            image_node["width"] = width_opt

        figure = nodes.figure()
        figure += image_node
        figure.setdefault("classes", []).extend(
            ["adaptive-figure", "polydiv-figure", "no-click"]
        )

        if "class" in self.options:
            figure["classes"].extend(self.options["class"])
        if "align" in self.options:
            figure["align"] = self.options["align"]
        else:
            figure["align"] = "center"

        # Figure-level width is less reliable; rely on image width + CSS only

        if self.content:
            caption_text = "\n".join(self.content)
            caption_node = nodes.caption()
            caption_node += nodes.Text(caption_text)
            figure += caption_node

        if explicit_name:
            self.add_name(figure)

        return [figure]


def setup(app):
    app.add_directive("polydiv", PolyDivDirective)
    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
