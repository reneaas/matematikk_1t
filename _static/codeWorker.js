// _static/codeWorker.js
importScripts('https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.js');

async function loadPyodideAndPackages() {
    self.pyodide = await loadPyodide();
    await self.pyodide.loadPackage(['numpy', 'sympy']);
}

loadPyodideAndPackages().then(() => {
    self.postMessage({ type: 'initialized' });
});

self.onmessage = async (event) => {
    const { python } = event.data;
    try {
        await self.pyodide.loadPackagesFromImports(python);
        const results = await self.pyodide.runPythonAsync(python);
        self.postMessage({ type: 'results', results });
    } catch (error) {
        self.postMessage({ type: 'error', error: error.message });
    }
};
