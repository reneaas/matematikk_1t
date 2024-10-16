// workerManager.js

class WorkerManager {
    static instance = null;

    static getInstance(preloadPackages = null) {
        if (!WorkerManager.instance) {
            WorkerManager.instance = new WorkerManager(preloadPackages);
        } else {
            // If preloadPackages is provided later, ensure the packages are loaded
            if (preloadPackages) {
                WorkerManager.instance.loadPackages(preloadPackages);
            }
        }
        return WorkerManager.instance;
    }

    constructor(preloadPackages = null) {
        if (WorkerManager.instance) {
            return WorkerManager.instance;
        }

        this.worker = null;
        this.callbacks = {}; // For managing callbacks with message IDs
        this.preloadPackages = preloadPackages;
        console.log("Preload packages in WorkerManager:", this.preloadPackages);
        this.initWorker();

        WorkerManager.instance = this;
    }

    initWorker() {
        const workerScript = `
importScripts('https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js');

let pyodideReadyPromise = loadPyodide();

async function resetPyodide(pyodide, initialGlobals) {
    const currentGlobals = new Set(pyodide.globals.keys());
    const globalsToClear = Array.from(currentGlobals).filter(x => !initialGlobals.has(x));
    for (const key of globalsToClear) {
        pyodide.globals.delete(key);
    }
}

onmessage = async (event) => {
    const messageId = event.data.messageId;
    if (event.data.type === 'init') {
        const pyodide = await pyodideReadyPromise;
        const initialGlobals = new Set(pyodide.globals.keys());
        postMessage(JSON.stringify({ type: 'initReady' }));
    }
    if (event.data.type === 'runCode') {
        const { code } = event.data;
        try {
            const pyodide = await pyodideReadyPromise;
            const initialGlobals = new Set(pyodide.globals.keys());
            await resetPyodide(pyodide, initialGlobals);

            // Prepare the Python code
            const pyCode = \`
import sys
import json
from js import postMessage

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
\`;

            await pyodide.runPythonAsync(pyCode);

            await pyodide.runPythonAsync(code);
            postMessage(JSON.stringify({ type: 'executionComplete', messageId }));
        } catch (err) {
            postMessage(JSON.stringify({ type: 'stderr', msg: String(err), messageId }));
        }
    }

    if (event.data.type === 'loadPackage') {
        const { packages } = event.data;
        try {
            const pyodide = await pyodideReadyPromise;
            console.log("Loading packages:", packages);
            await pyodide.loadPackage(packages);
            console.log("Packages loaded:", packages);
            postMessage(JSON.stringify({ type: 'packagesLoaded' }));
        } catch (err) {
            postMessage(JSON.stringify({ type: 'stderr', msg: String(err), messageId }));
        }
    }
};
`;

        const workerBlob = new Blob([workerScript], { type: 'application/javascript' });
        this.worker = new Worker(URL.createObjectURL(workerBlob));

        this.worker.onmessage = this.handleMessage.bind(this);
        this.worker.onerror = this.handleError.bind(this);

        this.worker.postMessage({ type: 'init' });
    }

    generateMessageId() {
        return 'msg-' + Math.random().toString(36).substr(2, 9);
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

        if (messageId && this.callbacks[messageId]) {
            this.callbacks[messageId](data);

            // Optionally remove the callback if execution is complete
            if (data.type === 'executionComplete') {
                delete this.callbacks[messageId];
            }
        } else {
            // Handle messages without messageId, like 'initReady' or 'packagesLoaded'
            if (data.type === 'initReady' || data.type === 'packagesLoaded') {
                console.log("Worker initialization message:", data.type);
            } else {
                console.warn("Unhandled message from worker:", data);
            }
        }
    }

    handleError(error) {
        console.error("Worker error:", error);
    }

    loadPackages(packages) {
        this.worker.postMessage({ type: 'loadPackage', packages });
    }

    restartWorker() {
        if (this.worker) {
            this.worker.terminate();
            this.worker = null;
        }

        this.initWorker();
    }
}
