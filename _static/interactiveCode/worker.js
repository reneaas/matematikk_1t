
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

    if (event.data.type === 'loadPackage') {
        const { packages } = event.data;
        try {
            await pyodide.loadPackage(packages);
            postMessage(JSON.stringify({ type: 'packagesLoaded' }));
        } catch (err) {
            postMessage(JSON.stringify({ type: 'stderr', msg: String(err)}));
        }
    }
};
