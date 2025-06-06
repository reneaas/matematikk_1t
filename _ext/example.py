from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging

logger = logging.getLogger(__name__)


class ExampleDirective(SphinxDirective):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self):
        title = self.arguments[0]

        # Create the admonition node
        admonition_node = nodes.admonition()
        admonition_node["classes"] = ["admonition", "example"]

        # Create the title node
        title_node = nodes.title()
        parsed_title, _ = self.state.inline_text(title, self.lineno)
        title_node += parsed_title
        admonition_node += title_node

        # Parse the content
        self.state.nested_parse(self.content, self.content_offset, admonition_node)

        return [admonition_node]


def setup(app):
    app.add_directive("example", ExampleDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
