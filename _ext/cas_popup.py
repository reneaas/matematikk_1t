from docutils import nodes
from sphinx.util.docutils import SphinxDirective
import uuid


class CASPopUpDirective(SphinxDirective):
    # Allow optional arguments: button text and dialog title
    required_arguments = 2  # width and height
    optional_arguments = 2  # button text and dialog title
    has_content = False

    def run(self):
        # Convert arguments to integers (with defaults if conversion fails)
        try:
            width = int(self.arguments[0])
        except ValueError:
            width = 700
        try:
            height = int(self.arguments[1])
        except ValueError:
            height = 400

        # Get optional arguments or use defaults
        button_text = self.arguments[2] if len(self.arguments) > 2 else "Åpne CAS-vindu"
        dialog_title = self.arguments[3] if len(self.arguments) > 3 else "CAS-vindu"

        # Generate a unique container ID using a short UUID
        container_id = f"ggb-cas-{uuid.uuid4().hex[:8]}"
        dialog_id = f"dialog-{container_id}"
        button_id = f"button-{container_id}"

        # Create the raw HTML with jQuery UI
        html = f"""
<!-- jQuery and jQuery UI -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="https://code.jquery.com/ui/1.13.2/jquery-ui.min.js"></script>
<link rel="stylesheet" href="https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css">

<!-- Button to open the dialog -->
<button id="{button_id}" class="ggb-cas-button">{button_text}</button>

<!-- Dialog that will contain the CAS applet -->
<div id="{dialog_id}" title="{dialog_title}" style="display:none;">
    <div id="{container_id}" style="width:{width}px;height:{height}px;" class="ggb-window"></div>
</div>

<script>
(function() {{
    
    // Once document is ready
    $(document).ready(function() {{
        var appletInitialized = false;
        var dialogPaddingV = 60;
        var dialogPaddingH = 20;
        
        // Dialog initialization
        $("#{dialog_id}").dialog({{
            autoOpen: false,
            width: {width + 40},
            height: {height + 80},
            modal: false,
            resizable: true,
            draggable: true,
            position: {{ my: "center", at: "center", of: window }},
            resize: function(event, ui) {{
                if (window.ggbApplet) {{
                    var newWidth = ui.size.width - dialogPaddingH;
                    var newHeight = ui.size.height - dialogPaddingV;
                    $("#{container_id}").css({{ width: newWidth + 'px', height: newHeight + 'px' }});
                    window.ggbApplet.setSize(newWidth, newHeight);
                }}
            }},
            open: function() {{
                // Initialize applet if not already done
                if (!appletInitialized) {{
                    var params = {{
                        appName: "classic",
                        width: {width},
                        height: {height},
                        showToolBar: true,
                        showAlgebraInput: true,
                        showMenuBar: false,
                        language: 'nb',
                        borderRadius: 8,
                        useBrowserForJS: false,
                        preventFocus: false,
                        showFullscreenButton: false,
                        showResetIcon: true,
                        enableRightClick: true,
                        showKeyboardOnFocus: false,
                        id: '{container_id}',
                        perspective: 'C',
                        'customToolBar': '1001 | 1002 | 1007 | 1010 | 1008 | 6',
                    }};
                    
                    var applet = new GGBApplet(params, true);
                    applet.inject('{container_id}');
                    appletInitialized = true;
                }}
            }}
        }});
        
        // Button click handler
        $("#{button_id}").button().on("click", function() {{
            $("#{dialog_id}").dialog("open");
        }});
    }});
}})();
</script>
        """
        return [nodes.raw("", html, format="html")]


def setup(app):
    app.add_directive("cas-popup", CASPopUpDirective)

    # Add jQuery UI CSS
    app.add_css_file("https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css")

    # Add custom CSS properly
    app.add_css_file("misc_styles/cas_popup.css")

    # Create a static path for custom CSS files if needed
    # app.connect("builder-inited", lambda app: create_custom_css(app))

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
