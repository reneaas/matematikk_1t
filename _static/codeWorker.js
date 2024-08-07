

let initialGlobals = new Set();
let cachedPyodide = null;
let packages = ["numpy", "sympy"];

const pyConsoleScript = `
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
`;


const customInputScript = (outputId) => `
    import builtins
    from js import document, window

    def input(prompt=""):
        try:
            output = document.getElementById("${outputId}")
            output.textContent += prompt
            user_input = window.prompt(prompt)
            if user_input is None:
                user_input = ""
            output.textContent += user_input + "\\n"
            return user_input
        except Exception as e:
            output.textContent += "Error: " + str(e) + "\\n"
            raise e

    builtins.input = input
`;



async function setupCustomIO(outputId) {
    await cachedPyodide.runPythonAsync(pyConsoleScript);
}

async function setupCustomInput(outputId) {
    await cachedPyodide.runPythonAsync(customInputScript(outputId));
}

async function initializePyodide() {
    if (!cachedPyodide) {
        console.log('Initializing Pyodide...');
        cachedPyodide = await loadPyodide();
        await cachedPyodide.loadPackage(packages);
        console.log('Pyodide initialized.');

        initialGlobals = new Set(cachedPyodide.globals.keys());
        console.log("Initial globals:", initialGlobals);
    }
}

async function resetPyodide() {
    const currentGlobals = new Set(cachedPyodide.globals.keys());
    const globalsToClear = Array.from(currentGlobals).filter(x => !initialGlobals.has(x));
    for (const key of globalsToClear) {
        cachedPyodide.globals.delete(key);
    }
    console.log("Globals cleared:", globalsToClear);
}

async function workerRunCode(code, outputId) {
    const output = document.getElementById(outputId);

    try {
        await initializePyodide();
        await resetPyodide();
        await setupCustomIO(outputId);

        if (code.includes('input(')) {
            await setupCustomInput(outputId);
        }

        await cachedPyodide.runPythonAsync(code);
        output.textContent = cachedPyodide.globals.get("sys").stdout.buffer;
    } catch (err) {
        output.innerHTML = formatErrorMessage(cachedPyodide.globals.get("sys").stderr.buffer);
        console.log("Error caught in JavaScript:", err);
    }
}


self.onmessage = async (event) => {
    const { cmd , code, outputId } = event.data;
    switch (cmd) {
        case "init":
            self.importScripts("https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js");
            await initializePyodide();
            break;

        
        case "run":
            await workerRunCode(code, outputId);
            break;
    }
};


