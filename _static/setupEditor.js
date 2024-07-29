async function initializePyodide() {
    console.log('Initializing Pyodide...');
    let pyodide = await loadPyodide();
    await pyodide.loadPackage('numpy');
    console.log('Pyodide initialized.');
    return pyodide;
}

async function setupEditor(pyodide, editorID, buttonID, outputId) {
    let editor = CodeMirror.fromTextArea(document.getElementById(editorID), {
        mode: "python",
        lineNumbers: true,
        theme: "night",
        tabSize: 4,
        indentUnit: 4,
    });

    let runButton = document.getElementById(buttonID);
    let output = document.getElementById(outputId);

    runButton.addEventListener("click", async () => {
        let code = editor.getValue();

        try {
            await pyodide.runPythonAsync(`
                from js import console
                import sys
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
        } catch (error) {
            output.textContent = error;
        }
    });
}

function setupIntersectionObserver(pyodide, editorID, buttonID, outputId) {
    let observer = new IntersectionObserver(async (entries) => {
        if (entries[0].isIntersecting) {
            observer.unobserve(document.getElementById(editorID));
            await setupEditor(pyodide, editorID, buttonID, outputId);
        }
    }, { threshold: 0.1 });

    observer.observe(document.getElementById(editorID));
}