let worker = null;

const pyConsoleScript = `
import sys
from js import postMessage
import json

class PyConsole:
    def __init__(self):
        self.buffer = ""

    def write(self, msg):
        self.buffer += msg
        if "\\n" in msg:
            self.flush()

    def flush(self):
        if self.buffer:
            try:
                postMessage(json.dumps({'type': 'stdout', 'msg': self.buffer}))
            except Exception as e:
                self.handle_error(e)

        self.buffer = ""

    def handle_error(self, e):
        error_message = str(e)
        postMessage(json.dumps({'type': 'stderr', 'msg': error_message}))

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


function initializeWorker(outputId) {
    const workerScript = `
        importScripts('https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js');

        let pyodideReadyPromise = loadPyodide();
        let pyodide;
        let firstrun = true;
        let initialGlobals = new Set();

        async function resetPyodide() {
            const currentGlobals = new Set(pyodide.globals.keys());
            const globalsToClear = Array.from(currentGlobals).filter(x => !initialGlobals.has(x));
            for (const key of globalsToClear) {
                pyodide.globals.delete(key);
            }
            console.log("Globals cleared:", globalsToClear);
        }


        onmessage = async (event) => {
            await pyodideReadyPromise;
            if (event.data.type === 'init') {
                pyodide = await pyodideReadyPromise;
                await pyodide.loadPackage(['numpy', 'sympy']);
                // postMessage({ type: 'initComplete', msg: 'Pyodide loaded' });  // Change here
            }
            if (event.data.type === 'runCode') {
                const { code } = event.data;
                try {
                    await resetPyodide();
                    await pyodide.runPythonAsync(code);
                } catch (err) {
                    postMessage({ type: 'stderr', 'msg': String(err) });
                }
            }
        };
    `;






    if (!worker) {
        const workerBlob = new Blob([workerScript], { type: 'application/javascript' });
        worker = new Worker(URL.createObjectURL(workerBlob));
    }

    worker.onmessage = function(event) {
        console.log("Received message:", event.data);  // Helpful for debugging
        let data;
        try {
            data = JSON.parse(event.data);
        } catch (e) {
            console.error("Failed to parse message data:", event.data);
            return;
        }
        const { type, msg } = data;
        const outputElement = document.getElementById(outputId);
        if (!outputElement) {
            console.error("Output element not found:", outputId);
            return;
        }
    
        if (type === 'stdout') {
            // Check if stdout contains error messages like SyntaxError
            if (/Error/.test(msg)) {
                outputElement.innerHTML += formatErrorMessage(msg); // Treat as error message
            } else {
                outputElement.innerHTML += msg;  // Append regular output
            }
        } else if (type === 'stderr') {
            outputElement.innerHTML += formatErrorMessage(msg); // Always format stderr messages
        }
    };

    worker.onerror = function(error) {
        console.log('Error from worker:', error);
        const outputElement = document.getElementById(outputId);
        if (outputElement) {
            outputElement.textContent += `Error: ${error.message}`;
        }
    };

    worker.postMessage({ type: 'init' });
}

async function runCode(editor, outputId) {
    const code = editor.getValue();
    worker.onmessage = function(event) {
        console.log("Received message:", event.data);  // Helpful for debugging
        let data;
        try {
            data = JSON.parse(event.data);
        } catch (e) {
            console.error("Failed to parse message data:", event.data);
            return;
        }
        const { type, msg } = data;
        const outputElement = document.getElementById(outputId);
        if (!outputElement) {
            console.error("Output element not found:", outputId);
            return;
        }
    
        if (type === 'stdout') {
            // Check if stdout contains error messages like SyntaxError
            if (/Error/.test(msg)) {
                outputElement.innerHTML += formatErrorMessage(msg); // Treat as error message
            } else {
                outputElement.innerHTML += msg;  // Append regular output
            }
        } else if (type === 'stderr') {
            outputElement.innerHTML += formatErrorMessage(msg); // Always format stderr messages
        }
    };

    // Ensure the worker is initialized before posting messages
    if (!worker) {
        initializeWorker(outputId);
    }

    // Run the pyConsoleScript first
    worker.postMessage({ type: 'runCode', code: pyConsoleScript });

    // If the code contains input, run the customInputScript
    // if (code.includes("input(")) {
    //     worker.postMessage({ type: 'runCode', code: customInputScript(outputId) });
    // }

    // Finally, run the user's code
    worker.postMessage({ type: 'runCode', code: code });
}

function getCurrentTheme() {
    const mode = document.documentElement.getAttribute('data-mode');
    const lightTheme = "github-light";
    const darkTheme = "github-dark-high-contrast";
    if (mode === 'dark') {
        return darkTheme;
    } else if (mode === 'light') {
        return lightTheme;
    } else if (mode === 'auto') {
        const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)').matches;
        return prefersDarkScheme ? darkTheme : lightTheme;
    }
}

function addcommentOverlayMode(editor) {
    editor.addOverlay({
        token: function(stream) {
            const keywords = ["# TODO", "# FIKSMEG", "# FIKS MEG", "# NOTE", "# FYLL INN"];
            for (const keyword of keywords) {
                if (stream.match(keyword)) {
                    return keyword.replace("# ", "").toLowerCase().replace(" ", "");
                }
            }
            while (stream.next() != null && !keywords.some(keyword => stream.match(keyword, false))) {}
            return null;
        }
    });
    return editor;
}

function getEditor(editorId) {
    let editor = CodeMirror.fromTextArea(document.getElementById(editorId), {
        mode: {
            name: "python",
            overlay: "commentOverlay",
        },
        lineNumbers: true,
        theme: getCurrentTheme(),
        tabSize: 4,
        indentUnit: 4,
        extraKeys: {
            Tab: function(cm) {
                let spaces = Array(cm.getOption("indentUnit") + 1).join(" ");
                cm.replaceSelection(spaces);
            }
        }
    });
    editor = addcommentOverlayMode(editor);
    return editor;
}

function setupEditor(editorId, runButtonId, cancelButtonId, resetButtonId, outputId) {
    let editor = getEditor(editorId);

    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            if (mutation.attributeName === 'data-mode') {
                editor.setOption('theme', getCurrentTheme());
            }
        });
    });

    observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['data-mode']
    });

    editor.setOption('theme', getCurrentTheme());

    let runButton = document.getElementById(runButtonId);
    if (runButton) {
        runButton.addEventListener("click", async () => {
            const outputElement = document.getElementById(outputId);
            if (outputElement) {
                outputElement.textContent = "";
            }
            await runCode(editor, outputId);
        });
    }

    let cancelButton = document.getElementById(cancelButtonId);
    if (cancelButton) {
        cancelButton.addEventListener("click", () => {
            if (worker) {
                worker.terminate();
                worker = null;
                initializeWorker(outputId);
            }
        });
    }

    let resetButton = document.getElementById(resetButtonId);
    if (resetButton) {
        resetButton.addEventListener("click", () => {
            editor.setValue(document.getElementById(editorId).value);
            const outputElement = document.getElementById(outputId);
            if (outputElement) {
                outputElement.textContent = "";
            }
        });
    }

    initializeWorker(outputId);
}



function formatErrorMessage(errorMsg) {
    let formattedMessage = errorMsg;

    // Highlight the error type
    const errorTypeMatch = errorMsg.match(/(\w+Error):/);
    if (errorTypeMatch) {
        formattedMessage = formattedMessage.replace(errorTypeMatch[1], `<span class="error-type">${errorTypeMatch[1]}</span>`);
    }

    // Highlight the line number in the pattern 'File "<exec>", line <number>'
    // formattedMessage = formattedMessage.replace(/line (\d+)/g, (match, p1) => {
    //     return match.replace(`line ${p1}`, `<span class="error-line">line ${p1}</span>`);
    // });

    return formattedMessage;
}



