from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives
import uuid


class PopupDirective(SphinxDirective):
    has_content = True
    option_spec = {
        "title": directives.unchanged,
        "width": directives.positive_int,
        "height": directives.positive_int,
    }
    required_arguments = 0
    optional_arguments = 1  # Button text

    def run(self):
        # Get button text from arguments or use default
        button_text = self.arguments[0] if self.arguments else "Vis mer"

        # Get title from options or use default
        dialog_title = self.options.get("title", "Mer informasjon")

        # Get width and height if specified
        width = self.options.get("width", 500)
        height = self.options.get("height", "auto")

        # Generate unique IDs
        popup_id = f"popup-{uuid.uuid4().hex[:8]}"
        button_id = f"button-{popup_id}"
        content_id = f"content-{popup_id}"

        # Process the directive content as markdown
        content_html = "\n".join(self.content)

        # Create the raw HTML with jQuery UI and KaTeX
        # Update the script loading part of your directive like this:

        html = f"""
<!-- Button to open the popup -->
<button id="{button_id}" class="popup-button">{button_text}</button>

<!-- Dialog container -->
<div id="{content_id}" class="popup-content" style="display:none;">
    {content_html}
</div>

<!-- Script for KaTeX and dialog setup -->
<script>
(function() {{
    // Function to load scripts sequentially
    function loadScript(src, id) {{
        return new Promise((resolve, reject) => {{
            // Check if script is already loaded
            if (document.getElementById(id)) {{
                resolve();
                return;
            }}
            
            const script = document.createElement('script');
            script.id = id;
            script.src = src;
            script.async = false; // Important: maintain loading order
            script.onload = () => resolve();
            script.onerror = () => reject(new Error(`Failed to load script: ${{src}}`));
            document.head.appendChild(script);
        }});
    }}
    
    // Function to load stylesheets
    function loadStylesheet(href, id) {{
        return new Promise((resolve) => {{
            if (document.getElementById(id)) {{
                resolve();
                return;
            }}
            
            const link = document.createElement('link');
            link.id = id;
            link.rel = 'stylesheet';
            link.href = href;
            link.onload = resolve;
            document.head.appendChild(link);
        }});
    }}
    
    // Initialize dialog once everything is loaded
    function initializeDialog() {{
        $("#{content_id}").dialog({{
            autoOpen: false,
            title: "{dialog_title}",
            width: {width},
            dialogClass: "popup-dialog",
            modal: false,
            resizable: true,
            draggable: true,
            open: function() {{
                // Safety check to ensure KaTeX is available
                if (window.katex && window.renderMathInElement) {{
                    try {{
                        renderMathInElement(document.getElementById('{content_id}'), {{
                            delimiters: [
                                {{left: "$$", right: "$$", display: true}},
                                {{left: "$", right: "$", display: false}},
                                {{left: "\\\\(", right: "\\\\)", display: false}},
                                {{left: "\\\\[", right: "\\\\]", display: true}}
                            ],
                            throwOnError: false
                        }});
                    }} catch (e) {{
                        console.error("KaTeX rendering error:", e);
                    }}
                }}
            }}
        }});
        
        // Button click handler
        $("#{button_id}").on("click", function() {{
            $("#{content_id}").dialog("open");
        }});
    }}
    
    // Main initialization function
    async function initialize() {{
        try {{
            // First, load jQuery if not already available
            if (!window.jQuery) {{
                await loadScript('https://code.jquery.com/jquery-3.6.0.min.js', 'jquery-script');
            }}
            
            // Then jQuery UI
            if (!window.jQuery.ui) {{
                await loadScript('https://code.jquery.com/ui/1.13.2/jquery-ui.min.js', 'jquery-ui-script');
                await loadStylesheet('https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css', 'jquery-ui-css');
            }}
            
            // Then KaTeX and auto-render in sequence
            await loadStylesheet('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css', 'katex-css');
            await loadScript('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js', 'katex-script');
            await loadScript('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js', 'katex-auto-render');
            
            // Initialize dialog after all scripts are loaded
            initializeDialog();
        }} catch (error) {{
            console.error('Error initializing popup:', error);
        }}
    }}
    
    // Start initialization when document is ready
    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', initialize);
    }} else {{
        initialize();
    }}
}})();
</script>
"""
        return [nodes.raw("", html, format="html")]


def setup(app):
    app.add_directive("popup", PopupDirective)

    # Add jQuery UI CSS
    app.add_css_file("https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css")

    # Add custom CSS for popup
    app.add_css_file("misc_styles/popup.css")

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
