// workerManager.js

class WorkerManager {
    static instance = null;

    // static getInstance(preloadPackages = null) {
    //     if (!WorkerManager.instance) {
    //         // Include 'matplotlib' in the default preloadPackages
    //         const defaultPreloadPackages = ['casify', 'matplotlib', 'micropip', 'numpy', 'scipy', 'sympy'];
    //         const combinedPreloadPackages = preloadPackages
    //             ? [...defaultPreloadPackages, ...preloadPackages]
    //             : defaultPreloadPackages;
    //         WorkerManager.instance = new WorkerManager(combinedPreloadPackages);
    //     } else {
    //         // If preloadPackages is provided later, ensure the packages are loaded
    //         if (preloadPackages) {
    //              // Include matplotlib in the set of packages.
    //              const packagesToLoad = ['casify', 'matplotlib', 'micropip', 'numpy', 'scipy', 'sympy', ...preloadPackages];
    //              WorkerManager.instance.loadPackages(packagesToLoad);
    //         }
    //     }
    //     return WorkerManager.instance;
    // }

    static getInstance(preloadPackages = null) {
        if (!WorkerManager.instance) {
            // Default PYODIDE packages (no custom packages here)
            const defaultPreloadPackages = ['matplotlib', 'numpy', 'scipy', 'sympy', 'micropip'];
            const combinedPreloadPackages = Array.from(new Set(preloadPackages ? [...defaultPreloadPackages, ...preloadPackages] : defaultPreloadPackages));
            WorkerManager.instance = new WorkerManager(combinedPreloadPackages);
        } else if (preloadPackages) {
            // Only load packages that are NOT already loaded.
            const packagesToLoad = preloadPackages.filter(pkg => !WorkerManager.instance.loadedPackages.has(pkg));
             const combinedPreloadPackages = Array.from(new Set(['matplotlib', 'numpy', 'scipy', 'sympy', ...packagesToLoad])); // Pyodide packages
            if (combinedPreloadPackages.length > 0) {
    
                WorkerManager.instance.loadPackages(combinedPreloadPackages);
            }
        }
        return WorkerManager.instance;
    }


    constructor(preloadPackages = null) { // Default to preloading matplotlib
        if (WorkerManager.instance) {
            return WorkerManager.instance;
        }

        this.worker = null;
        this.callbacks = {}; // For managing callbacks with message IDs
        this.preloadPackages = preloadPackages;
        this.loadedPackages = new Set();
        this.packageLoadPromises = {}; // Map of packageRequestId to {resolve, reject, packages}
        console.log("Preload packages in WorkerManager:", this.preloadPackages);

        // Create a promise that resolves when the worker is ready and preloadPackages are loaded
        this.workerReadyPromise = new Promise((resolve, reject) => {
            this.workerReadyResolve = resolve;
            this.workerReadyReject = reject;
        });

        this.initWorker();

        WorkerManager.instance = this;
    }

    initWorker() {
        const workerScript = `
importScripts('https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js');

let pyodideReadyPromise = loadPyodide();
let initialGlobals = new Set();

async function resetPyodide(pyodide, initialGlobals) {
    const currentGlobals = new Set(pyodide.globals.keys());
    const globalsToClear = Array.from(currentGlobals).filter(x => !initialGlobals.has(x));
    for (const key of globalsToClear) {
        pyodide.globals.delete(key);
    }
    console.log("Globals cleared:", globalsToClear);
}

// Helper function to install packages via micropip
async function installPackages(pyodide, packages) {
    if (packages.length > 0) {
        await pyodide.loadPackage("micropip"); // Load micropip
        const micropip = pyodide.pyimport("micropip");
        await micropip.install(packages);
        await micropip.install("casify");
        await micropip.install("plotmath");
        await micropip.install("signchart");
    }
}

onmessage = async (event) => {
    const messageId = event.data.messageId;
    if (event.data.type === 'init') {
        const pyodide = await pyodideReadyPromise;
        await pyodide.loadPackage("micropip");
        // await installPackages(pyodide, event.data.preloadPackages || []);
        
        initialGlobals = new Set(pyodide.globals.keys());
        postMessage(JSON.stringify({ type: 'initReady' }));
    }

    
    if (event.data.type === 'runCode') {
        const { code } = event.data;
        try {
            const pyodide = await pyodideReadyPromise;
            await resetPyodide(pyodide, initialGlobals);

            // Prepare the Python code
            const pyCode = \`
import sys
import json
import micropip
import io
import base64
from js import postMessage
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class PyConsole:
    def __init__(self, messageId):
        self.messageId = messageId
        self.buffer = ""

    def write(self, msg):
        self.buffer += msg
        if "\\\\n" in msg:
            self.flush()

    def flush(self):
        if self.buffer:
            postMessage(json.dumps({'type': 'stdout', 'msg': self.buffer, 'messageId': self.messageId}))
            self.buffer = ""

sys.stdout = PyConsole("\${messageId}")
sys.stderr = PyConsole("\${messageId}")

# Override plt.show()
def show_override(messageId):
    buf = io.BytesIO()
    plt.savefig(buf, format='png')

    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    postMessage(json.dumps({
        'type': 'plot',
        'data': image_base64,
        'messageId': messageId
    }))
    plt.clf() # Clear the figure after sending

plt.show = lambda: show_override("\${messageId}")
\`;

            await pyodide.runPythonAsync(pyCode);

            await pyodide.runPythonAsync(code);
            postMessage(JSON.stringify({ type: 'executionComplete', messageId }));
        } catch (err) {
            postMessage(JSON.stringify({ type: 'stderr', msg: String(err), messageId }));
        }
    }

    if (event.data.type === 'loadPackage') {
        const { packages, packageRequestId } = event.data;
        try {
            const pyodide = await pyodideReadyPromise;
            console.log("Loading packages:", packages);
            const filteredPackages = packages.filter(pkg => pkg !== "casify");
            await pyodide.loadPackage(filteredPackages);

            // Custom installation of casify package if present in the package list.
            if (packages.includes('casify')) {
                await pyodide.loadPackage("micropip");
                await pyodide.runPythonAsync("import micropip; await micropip.install('casify')");
            }
            if (packages.includes('plotmath')) {
                await pyodide.loadPackage("micropip");
                await pyodide.runPythonAsync("import micropip; await micropip.install('plotmath')");
            }
            if (packages.includes('signchart')) {
                await pyodide.loadPackage("micropip");
                await pyodide.runPythonAsync("import micropip; await micropip.install('signchart')");
            }

            console.log("Packages loaded:", packages);
            postMessage(JSON.stringify({ type: 'packagesLoaded', packageRequestId }));
        } catch (err) {
            postMessage(JSON.stringify({ type: 'stderr', msg: String(err), packageRequestId }));
        }
    }
};
`;

        const workerBlob = new Blob([workerScript], { type: 'application/javascript' });
        this.worker = new Worker(URL.createObjectURL(workerBlob));

        this.worker.onmessage = this.handleMessage.bind(this);
        this.worker.onerror = this.handleError.bind(this);

        this.worker.postMessage({ type: 'init', preloadPackages: this.preloadPackages });
    }

    generateMessageId() {
        return 'msg-' + Math.random().toString(36).substr(2, 9);
    }

    loadPackages(packages) {
        const packagesToLoad = packages.filter(pkg => !this.loadedPackages.has(pkg));

        if (packagesToLoad.length === 0) {
            // All packages are already loaded
            return Promise.resolve();
        }

        // Create a unique ID for this package load request
        const packageRequestId = 'pkg-' + Math.random().toString(36).substr(2, 9);

        return new Promise((resolve, reject) => {
            // Store the resolve and reject functions
            this.packageLoadPromises[packageRequestId] = { resolve, reject, packages: packagesToLoad };
            this.worker.postMessage({ type: 'loadPackage', packages: packagesToLoad, packageRequestId });
        });
    }

    runCode(code, onMessageCallback) {
        const messageId = this.generateMessageId();
        this.callbacks[messageId] = onMessageCallback;
        this.worker.postMessage({ type: 'runCode', code, messageId });
        return messageId;
    }

    handleMessage(event) {
        let data;
        try {
            data = JSON.parse(event.data);
        } catch (e) {
            console.error("Failed to parse message from worker:", event.data);
            return;
        }

        const messageId = data.messageId;
        const packageRequestId = data.packageRequestId;

        if (messageId && this.callbacks[messageId]) {
            this.callbacks[messageId](data);

            if (data.type === 'executionComplete') {
                delete this.callbacks[messageId];
            }
        } else if (packageRequestId && this.packageLoadPromises[packageRequestId]) {
            const packagePromise = this.packageLoadPromises[packageRequestId];
            if (data.type === 'packagesLoaded') {
                // Mark packages as loaded
                for (const pkg of packagePromise.packages) {
                    this.loadedPackages.add(pkg);
                }
                packagePromise.resolve();
            } else if (data.type === 'stderr') {
                packagePromise.reject(new Error(data.msg));
            }
            delete this.packageLoadPromises[packageRequestId];
        } else {
            // Handle messages without messageId, like 'initReady'
            if (data.type === 'initReady') {
                console.log("Worker initialization message:", data.type);
                // Now load preloadPackages if any
                if (this.preloadPackages && this.preloadPackages.length > 0) {
                    this.loadPackages(this.preloadPackages)
                        .then(() => {
                            console.log("Preload packages loaded:", this.preloadPackages);
                            this.workerReadyResolve();
                        })
                        .catch((err) => {
                            console.error("Failed to load preload packages:", err);
                            this.workerReadyReject(err);
                        });
                } else {
                    this.workerReadyResolve();
                }
            } else {
                console.warn("Unhandled message from worker:", data);
            }
        }
    }

    handleError(error) {
        console.error("Worker error:", error);
        if (this.workerReadyReject) {
            this.workerReadyReject(error);
        }
    }

    restartWorker() {
        if (this.worker) {
            this.worker.terminate();
            this.worker = null;
        }

        // Reset loaded packages and create a new workerReadyPromise
        this.loadedPackages = new Set();
        this.workerReadyPromise = new Promise((resolve, reject) => {
            this.workerReadyResolve = resolve;
            this.workerReadyReject = reject;
        });

        this.initWorker();
    }
}
