// Setter opp pyodide
async function initializePyodide() {
    console.log('Initializing Pyodide...');
    let pyodide = await loadPyodide();
    await pyodide.loadPackage('numpy');
    console.log('Pyodide initialized.');
    return pyodide;
}

// Setter opp code editor med code mirror
async function setupEditor(pyodide, editorId, buttonId, outputId) {
    let editor = CodeMirror.fromTextArea(document.getElementById(editorId), {
        mode: "python",
        lineNumbers: true,
        theme: "midnight", // Other themes at https://codemirror.net/5/demo/theme.html#default
        tabSize: 4,
        indentUnit: 4,
        fontSize: 30,
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

// Lazy load the editor and Pyodide when the editor comes into view
function lazyLoadEditor(editorId, buttonId, outputId) {
    const editorElement = document.getElementById(editorId);
    const observer = new IntersectionObserver(async (entries, observer) => {
        entries.forEach(async entry => {
            if (entry.isIntersecting) {
                observer.unobserve(entry.target);
                let pyodide = await initializePyodide();
                await setupEditor(pyodide, editorId, buttonId, outputId);
            }
        });
    }, { threshold: 0.1 });

    observer.observe(editorElement);
}