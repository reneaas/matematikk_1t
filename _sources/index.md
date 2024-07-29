# Matematikk 1T

Velkommen til ditt første programfag på videregående skole ved Edvard Munch Vgs! 

Matematikk 1T kommer til å by på mange nye utfordringer som du ikke har møtt i matematikken tidligere.
Det er mange nye begreper og matematiske ideer som vil oppleves som abstrakte og vanskelige å forstå i starten. 
Men hold ut og jobb masse med faget, så kommer du ut på andre siden med en opplevelse av å ha mestret en av de største utfordringene du har møtt til nå! 


## Innhold
:::{tableofcontents}
:::


# Interactive Python with Pyodide and CodeMirror

Below is an interactive Python code editor using Pyodide and CodeMirror.

```{raw} html
<div>
    <textarea id="code-editor" name="code">
def f(x):
    return x**2 - 2*x + 3

x = 2
y = f(x)
print(y)
    </textarea>
    <button id="run-button">Run</button>
</div>
<pre id="output"></pre>

<script type="text/javascript">
    async function main() {
        // Load Pyodide
        let pyodide = await loadPyodide();

        // Initialize CodeMirror
        let editor = CodeMirror.fromTextArea(document.getElementById("code-editor"), {
            mode: "python",
            lineNumbers: true,
            theme: "nord",
            tabSize: 4,
            indentUnit: 4,
        });

        // Get references to the HTML elements
        let runButton = document.getElementById("run-button");
        let output = document.getElementById("output");

        // Add an event listener to the run button
        runButton.addEventListener("click", async () => {
            // Get the code from the editor
            let code = editor.getValue();

            // Run the Python code and capture the output
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
                output.textContent = err;
            }
        });
    }

    // Call the main function to set everything up
    main();
</script>
```