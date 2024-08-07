let packages = ["numpy", "sympy"];
let cachedPyodide = null;
let initialGlobals = new Set();
let initialCode = null;


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

async function runCode(editor, outputId) {
    const code = editor.getValue();
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

function setupEditor(editorId, buttonId, resetButtonId, outputId) {
    let editor = getEditor(editorId);
    // initialCode = editor.getValue(); // Save initial code
    // console.log("Initial code:", initialCode);

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

    let runButton = document.getElementById(buttonId);
    runButton.addEventListener("click", async () => {
        await runCode(editor, outputId);
    });

    let output = document.getElementById(outputId);
    let resetButton = document.getElementById(resetButtonId);
    resetButton.addEventListener("click", () => {
        editor.setValue(document.getElementById(editorId).value);
        output.textContent = "";
    });

    cachedPyodide = initializePyodide();
}

function formatErrorMessage(errorMsg) {
    let formattedMessage = errorMsg;

    const errorTypeMatch = errorMsg.match(/(\w+Error):/);
    if (errorTypeMatch) {
        formattedMessage = formattedMessage.replace(errorTypeMatch[1], `<span class="error-type">${errorTypeMatch[1]}</span>`);
    }

    const lineNumberMatches = [...errorMsg.matchAll(/\bline (\d+)\b/g)];
    if (lineNumberMatches.length > 0) {
        const lastLineNumberMatch = lineNumberMatches[lineNumberMatches.length - 1];
        const secondLastLineNumberMatch = lineNumberMatches[lineNumberMatches.length - 2];

        if (errorTypeMatch) {
            const errorLineIndex = errorTypeMatch.index;
            const errorLineEndIndex = formattedMessage.indexOf('\n', errorLineIndex) === -1 ? formattedMessage.length : formattedMessage.indexOf('\n', errorLineIndex);
            const errorLine = formattedMessage.slice(errorLineIndex, errorLineEndIndex);
            const lineNumberInErrorLine = errorLine.match(/\bline (\d+)\b/);

            if (lineNumberInErrorLine && secondLastLineNumberMatch) {
                formattedMessage = highlightLineNumber(formattedMessage, secondLastLineNumberMatch);
            } else {
                formattedMessage = highlightLineNumber(formattedMessage, lastLineNumberMatch);
            }
        } else {
            formattedMessage = highlightLineNumber(formattedMessage, lastLineNumberMatch);
        }
    }

    return formattedMessage;
}

function highlightLineNumber(message, match) {
    return message.slice(0, match.index) + message.slice(match.index).replace(`line ${match[1]}`, `<span class="error-line">line ${match[1]}</span>`);
}