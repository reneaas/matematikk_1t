document.addEventListener("DOMContentLoaded", function() {
    // Select all code blocks
    const codeBlocks = document.querySelectorAll('.highlight .c1');

    codeBlocks.forEach(function(block) {
        // Check if the comment starts with "# TODO"
        if (block.textContent.trim().startsWith('# TODO')) {
            block.style.color = '#ff0000';
            block.style.fontWeight = 'bold';
        }
        // Check if the comment starts with "# FIKSMEG"
        if (block.textContent.trim().startsWith('# FIKSMEG')) {
            block.style.color = '#ff0000';
            block.style.fontWeight = 'bold';
        }
        // Check if the comment starts with "# NOTE"
        if (block.textContent.trim().startsWith('# NOTE')) {
            block.style.color = '#ff7b72';
            block.style.fontWeight = 'bold';
        }
    });
});



// Setter opp pyodide
async function initializePyodide() {
    let pyodide = await loadPyodide();
    await pyodide.loadPackage('numpy');
    return pyodide;
}

// Setter opp code editor med code mirror
async function setupEditor(pyodide, editorId, buttonId, outputId) {
    let editor = CodeMirror.fromTextArea(document.getElementById(editorId), {
        mode: "python",
        lineNumbers: true,
        theme: "night", // Other themes at https://codemirror.net/5/demo/theme.html#default
        tabSize: 4,
        indentUnit: 4,
    });
    
    let runButton = document.getElementById(buttonId);
    let output = document.getElementById(outputId);

    runButton.addEventListener("click", async () => {
        let code = editor.getValue();

        try {
            pyodide.runPythonAsync(`
                import sys
                from js import console
                class PyConsole:
                    def __init__(self):
                        self.buffer = ""
                    def write(self, msg):
                        self.buffer += msg
                    def flush(self):
                        console.log(self.buffer)
                        self.buffer = ""

                sys.stdout = PyConsole()
                sys.stderr = PyConsole()
            `);
            await pyodide.runPythonAsync(code);
            let result = pyodide.globals.get("sys").stdout.buffer;
            output.textContent = result;
        } catch (err) {
            output.textContent =  err;
        }
    });
}

