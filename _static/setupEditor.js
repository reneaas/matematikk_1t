function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            func.apply(this, args);
        }, wait);
    };
}

// Setter opp pyodide og cacher den for gjentatt bruk.
let packages = ["numpy", "sympy"]
let cachedPyodide = null;
let initialGlobals = new Set();
let firstRun = true;
async function initializePyodide() {
    if (!cachedPyodide) {
        console.log('Initializing Pyodide...');
        cachedPyodide = await loadPyodide();
        await cachedPyodide.loadPackage(packages);
        console.log('Pyodide initialized.');
    }
    return cachedPyodide;
}



async function resetPyodide() {
    const currentGlobals = new Set(cachedPyodide.globals.keys());
    const globalsToClear = Array.from(currentGlobals).filter(x => !initialGlobals.has(x));
    for (const key of globalsToClear) {
        cachedPyodide.globals.delete(key);
    }
}


// Setter opp code editor med code mirror
function setupEditor(editorId, buttonId, outputId) {
    const lightTheme = "github-light";
    const darkTheme = "github-dark-high-contrast";

    function getCurrentTheme() {
        const mode = document.documentElement.getAttribute('data-mode');
        // console.log("Mode: " + mode); // Debugging line for check `mode` value

        if (mode === 'dark') {
            return darkTheme;
        } else if (mode === 'light') {
            return lightTheme;
        } else if (mode === 'auto') {
            const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)').matches;
            return prefersDarkScheme ? darkTheme : lightTheme;
        }
    }

    console.log("Current theme: " + getCurrentTheme()); // Debugging line to check current theme

    let editor = CodeMirror.fromTextArea(document.getElementById(editorId), {
        mode: "python",
        lineNumbers: true,
        theme: getCurrentTheme(), // Other themes at https://codemirror.net/5/demo/theme.html#default
        tabSize: 4,
        indentUnit: 4,
        extraKeys: {
            Tab: function(cm) {
                let spaces = Array(cm.getOption("indentUnit") + 1).join(" ");
                cm.replaceSelection(spaces);
            }
        } // Sikrer at tab gir 4 spaces. Unngår utilsiktede bugs med innrykk.
    });

    // Apply the overlay mode
    editor.addOverlay({
        token: function(stream, state) {
            if (stream.match("# TODO")) {
                return "todo";
            } else if (stream.match("# FIKSMEG")) {
                return "fiksmeg";
            } else if (stream.match("# FIKS MEG")) {
                return "fiksmeg";
            } else if (stream.match("# NOTE")) {
                return "note";
            } else if (stream.match("# FYLL INN")) {
                return "fyllinn";
            }
            while (stream.next() != null && 
                !stream.match("# TODO", false) && 
                !stream.match("# FIKSMEG", false) && 
                !stream.match("# FIKS MEG", false) && 
                !stream.match("# NOTE", false) && 
                !stream.match("# FYLL INN", false)) {}
            return null;
        }
    });

    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            if (mutation.attributeName === 'data-mode') {
                // console.log('data-mode attribute changed'); // Debugging line to check attribute change
                editor.setOption('theme', getCurrentTheme());
            }
        });
    });

    // Start observing the document's data-mode attribute for changes
    observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['data-mode']
    });

    // Initial theme setup
    editor.setOption('theme', getCurrentTheme());

    let runButton = document.getElementById(buttonId);
    let output = document.getElementById(outputId);

    runButton.addEventListener("click", async () => {
        let code = editor.getValue();
        console.log("Running code:", code);

        try {
            await cachedPyodide.runPythonAsync(`
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

            if (code.includes('input(')) {
                await cachedPyodide.runPythonAsync(`
                    import builtins
                    from js import document, window

                    def input(prompt=""):
                        try:
                            output = document.getElementById("${outputId}")
                            output.textContent += prompt  # Display the prompt text in the output element
                            user_input = window.prompt(prompt)
                            if user_input is None:
                                user_input = ""
                            output.textContent += user_input + "\\n"  # Append the user input to the output element
                            return user_input
                        except Exception as e:
                            output.textContent += "Error: " + str(e) + "\\n"
                            raise e

                    builtins.input = input
                `);
            }

            if (firstRun) {
                initialGlobals = new Set(cachedPyodide.globals.keys());
                firstRun = false;
            }
            else {
                await resetPyodide();
            }
            await cachedPyodide.runPythonAsync(code);
            
            let result = cachedPyodide.globals.get("sys").stdout.buffer;
            output.textContent = result;
        } catch (err) {
            let errorMsg = cachedPyodide.globals.get("sys").stderr.buffer;
            output.innerHTML = formatErrorMessage(errorMsg);  // Call to format the error message
            // output.textContent = `Error: ${errorMsg}`;
            console.log("Error caught in JavaScript:", err);
        }
    });
    cachedPyodide = initializePyodide();
}



// function formatErrorMessage(errorMsg) {
//     // Match and highlight the error type
//     let errorTypeMatch = errorMsg.match(/(\w+Error):/);
//     let formattedMessage = errorMsg;

//     if (errorTypeMatch) {
//         formattedMessage = formattedMessage.replace(errorTypeMatch[1], `<span class="error-type">${errorTypeMatch[1]}</span>`);
//     }

//     // Match and highlight the exact last occurrence of "line <number>"
//     let lineNumberMatches = [...errorMsg.matchAll(/\bline (\d+)\b/g)];
//     if (lineNumberMatches.length > 0) {
//         let lastLineNumberMatch = lineNumberMatches[lineNumberMatches.length - 1];
//         formattedMessage = formattedMessage.slice(0, lastLineNumberMatch.index) +
//             formattedMessage.slice(lastLineNumberMatch.index).replace(`line ${lastLineNumberMatch[1]}`, `<span class="error-line">line ${lastLineNumberMatch[1]}</span>`);
//     }

//     return `<div class="error-message">${formattedMessage}</div>`;
// }



function formatErrorMessage(errorMsg) {
    // Match and highlight the error type
    let errorTypeMatch = errorMsg.match(/(\w+Error):/);
    let formattedMessage = errorMsg;

    if (errorTypeMatch) {
        formattedMessage = formattedMessage.replace(errorTypeMatch[1], `<span class="error-type">${errorTypeMatch[1]}</span>`);
    }

    // Match and highlight the exact occurrence of "line <number>"
    let lineNumberMatches = [...errorMsg.matchAll(/\bline (\d+)\b/g)];
    if (lineNumberMatches.length > 0) {
        let lastLineNumberMatch = lineNumberMatches[lineNumberMatches.length - 1];
        let secondLastLineNumberMatch = lineNumberMatches[lineNumberMatches.length - 2];
        
        // Check if line <number> exists in the same line as <type>Error
        if (errorTypeMatch) {
            let errorLineIndex = errorTypeMatch.index;
            let errorLineEndIndex = formattedMessage.indexOf('\n', errorLineIndex);
            errorLineEndIndex = errorLineEndIndex === -1 ? formattedMessage.length : errorLineEndIndex;
            
            let errorLine = formattedMessage.slice(errorLineIndex, errorLineEndIndex);
            let lineNumberInErrorLine = errorLine.match(/\bline (\d+)\b/);
            
            if (lineNumberInErrorLine) {
                // Highlight the second last occurrence if line <number> exists in the error line
                if (secondLastLineNumberMatch) {
                    formattedMessage = formattedMessage.slice(0, secondLastLineNumberMatch.index) +
                        formattedMessage.slice(secondLastLineNumberMatch.index).replace(`line ${secondLastLineNumberMatch[1]}`, `<span class="error-line">line ${secondLastLineNumberMatch[1]}</span>`);
                }
            } else {
                // Highlight the last occurrence otherwise
                formattedMessage = formattedMessage.slice(0, lastLineNumberMatch.index) +
                    formattedMessage.slice(lastLineNumberMatch.index).replace(`line ${lastLineNumberMatch[1]}`, `<span class="error-line">line ${lastLineNumberMatch[1]}</span>`);
            }
        } else {
            // Highlight the last occurrence otherwise
            formattedMessage = formattedMessage.slice(0, lastLineNumberMatch.index) +
                formattedMessage.slice(lastLineNumberMatch.index).replace(`line ${lastLineNumberMatch[1]}`, `<span class="error-line">line ${lastLineNumberMatch[1]}</span>`);
        }
    }

    return `<div class="error-message">${formattedMessage}</div>`;
}