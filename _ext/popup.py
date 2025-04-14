from docutils import nodes
from sphinx.util.docutils import SphinxDirective, SphinxRole
from docutils.parsers.rst import directives
import uuid
import re


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
            
            // Then jQuery UI - safer check
            if (!window.jQuery || typeof window.jQuery.ui === 'undefined') {{
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


class PopupRole(SphinxRole):
    def run(self):
        text = self.text  # The text inside the role

        # Check if there's content specified in options
        has_content = False
        content_html = ""
        popup_title = "💡"
        width = 400  # Default width

        # Check for options in format {popup}`text <content>` (title="Title")
        options_match = re.search(r"<([^>]+)>\s*(?:\(([^)]+)\))?", self.text)
        if options_match:
            # Extract the visible text and content
            text = self.text[: options_match.start()].strip()
            content_html = options_match.group(1)

            # Look for title and width in options
            if options_match.group(2):
                options = options_match.group(2)
                title_match = re.search(r'title="([^"]+)"', options)
                if title_match:
                    popup_title = title_match.group(1)

                width_match = re.search(r'width="(\d+)"', options)
                if width_match:
                    width = int(width_match.group(1))

            has_content = True

        # Generate unique IDs
        popup_id = f"popup-role-{uuid.uuid4().hex[:8]}"
        content_id = f"content-{popup_id}"
        script_id = f"script-{popup_id}"
        safe_id = popup_id.replace("-", "_")

        # Create HTML for the clickable text with proper namespacing
        html = f"""
<span class="popup-text math-content" data-popup-id="{popup_id}" id="text-{popup_id}">
    {text}
</span>
<div id="{content_id}" class="popup-content" style="display:none;" title="{popup_title}">
    {content_html}
</div>

<script id="{script_id}">
(function() {{
    // Create namespace unique to this instance to avoid conflicts
    const popup_{safe_id} = {{
        // Load scripts only if needed
        loadScript: function(src, id) {{
            return new Promise((resolve, reject) => {{
                if (document.getElementById(id)) {{
                    resolve();
                    return;
                }}
                
                const script = document.createElement('script');
                script.id = id;
                script.src = src;
                script.async = false;
                script.onload = () => resolve();
                script.onerror = () => reject(new Error(`Failed to load script: ${{src}}`));
                document.head.appendChild(script);
            }});
        }},
        
        loadStylesheet: function(href, id) {{
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
        }},

        renderMath: function() {{
            // Try to render math immediately if KaTeX is available
            if (window.katex && window.renderMathInElement) {{
                this.doRenderMath();
            }} else {{
                // If KaTeX isn't ready yet, wait and retry after a delay
                console.log("KaTeX not ready for {popup_id}, will retry...");
                setTimeout(() => {{
                    if (window.katex && window.renderMathInElement) {{
                        console.log("Retrying KaTeX render for {popup_id}");
                        this.doRenderMath();
                    }} else {{
                        console.error("KaTeX still not available for {popup_id} after delay");
                    }}
                }}, 500);
            }}
        }},

        doRenderMath: function() {{
            try {{
                const clickableText = document.getElementById("text-{popup_id}");
                if (clickableText) {{
                    renderMathInElement(clickableText, {{
                        delimiters: [
                            {{left: "$$", right: "$$", display: true}},
                            {{left: "$", right: "$", display: false}},
                            {{left: "\\\\(", right: "\\\\)", display: false}},
                            {{left: "\\\\[", right: "\\\\]", display: true}}
                        ],
                        throwOnError: false
                    }});
                    console.log("Math rendered successfully for {popup_id}");
                }}
            }} catch (e) {{
                console.error("KaTeX rendering error for {popup_id}:", e);
            }}
        }},
        
        initializePopup: function() {{
            const clickableText = document.getElementById("text-{popup_id}");
            if (!clickableText) {{
                console.error("Cannot find clickable text element for {popup_id}");
                return;
            }}
            
            let wasClicked = false;
            let isHovering = false;
            let hoverTimeout;
            
            // Initialize the dialog with specific selectors
            $("#{content_id}").dialog({{
                autoOpen: false,
                title: "{popup_title}",
                width: {width},
                dialogClass: "popup-dialog hover-dialog popup-{safe_id}", // Add unique class
                modal: false,
                resizable: true,
                draggable: true,
                position: {{ my: "center top", at: "center bottom", of: clickableText }},
                open: function() {{
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
                            console.error("KaTeX rendering error for {popup_id}:", e);
                        }}
                    }}
                }},
                close: function() {{
                    // Reset click state when dialog is closed
                    wasClicked = false;
                }}
            }});
            
            function getDialogElement() {{
                return document.querySelector(".ui-dialog.popup-{safe_id}");
            }}
            
            // Mouse enter - open dialog after a short delay
            clickableText.addEventListener('mouseenter', function(e) {{
                e.preventDefault();
                isHovering = true;
                clearTimeout(hoverTimeout);
                hoverTimeout = setTimeout(function() {{
                    if (isHovering && !wasClicked) {{
                        $("#{content_id}").dialog("open");
                    }}
                }}, 300);
            }});
            
            // Mouse leave - close dialog if it wasn't clicked
            clickableText.addEventListener('mouseleave', function(e) {{
                e.preventDefault();
                isHovering = false;
                clearTimeout(hoverTimeout);
                
                // Small delay to allow moving mouse to the dialog
                setTimeout(function() {{
                    if (!wasClicked && !popup_{safe_id}.isDialogHovered()) {{
                        $("#{content_id}").dialog("close");
                    }}
                }}, 300);
            }});
            
            // Click handler - open dialog and mark as clicked
            clickableText.addEventListener('click', function() {{
                wasClicked = true;
                $("#{content_id}").dialog("open");
            }});
            
            // Add hover detection to the dialog
            $(document).on('mouseenter', '.ui-dialog.popup-{safe_id}', function() {{
                isHovering = true;
            }}).on('mouseleave', '.ui-dialog.popup-{safe_id}', function() {{
                isHovering = false;
                setTimeout(function() {{
                    if (!wasClicked && !isHovering) {{
                        $("#{content_id}").dialog("close");
                    }}
                }}, 100);
            }});
        }},
        
        // Function to check if the mouse is over the dialog
        isDialogHovered: function() {{
            const dialogElement = document.querySelector(".ui-dialog.popup-{safe_id}");
            if (!dialogElement) return false;
            
            // Get current mouse position from event or fallback to stored position
            const mouseX = window.mouseX || 0;
            const mouseY = window.mouseY || 0;
            
            // Get dialog position
            const rect = dialogElement.getBoundingClientRect();
            
            // Check if mouse is inside dialog
            return (
                mouseX >= rect.left &&
                mouseX <= rect.right &&
                mouseY >= rect.top &&
                mouseY <= rect.bottom
            );
        }},
        
        initialize: async function() {{
            try {{
                // First, ensure jQuery is loaded
                if (!window.jQuery) {{
                    await this.loadScript('https://code.jquery.com/jquery-3.6.0.min.js', 'jquery-script');
                }}
                
                // Then check for jQuery UI more safely
                if (!window.jQuery || typeof window.jQuery.ui === 'undefined') {{
                    await this.loadScript('https://code.jquery.com/ui/1.13.2/jquery-ui.min.js', 'jquery-ui-script');
                    await this.loadStylesheet('https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css', 'jquery-ui-css');
                }}
                
                // Then load KaTeX if needed
                if (!window.katex) {{
                    await this.loadStylesheet('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css', 'katex-css');
                    await this.loadScript('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js', 'katex-script');
                    await this.loadScript('https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js', 'katex-auto-render');
                }}
                
                // Initialize popup first
                this.initializePopup();
                
                // Then render math after KaTeX is ready
                setTimeout(() => {{
                    this.renderMath();
                }}, 200);
                
                console.log("Popup {popup_id} initialized successfully");
            }} catch (error) {{
                console.error('Error initializing popup role {popup_id}:', error);
            }}
        }}
    }};
    
    // Track mouse position for hover detection
    document.addEventListener('mousemove', function(e) {{
        window.mouseX = e.clientX;
        window.mouseY = e.clientY;
    }});
    
    // Initialize this specific popup instance
    if (document.readyState === 'loading') {{
        document.addEventListener('DOMContentLoaded', function() {{
            popup_{safe_id}.initialize();
        }});
    }} else {{
        popup_{safe_id}.initialize();
    }}
}})();
</script>
"""

        # Create a raw node with the HTML
        node = nodes.raw("", html, format="html")
        return [node], []


def setup(app):
    app.add_directive("popup", PopupDirective)
    app.add_role("popup", PopupRole())

    # Add CSS file for jQuery UI
    app.add_css_file("https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css")

    # Add custom CSS for popups if needed
    # app.add_css_file("misc_styles/popup.css")

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
