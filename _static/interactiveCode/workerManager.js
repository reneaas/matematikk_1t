class WorkerManager {
    constructor(preloadPackages = null) {
        this.isInitialized = false;
        this.worker = null;
        this.pyoidideReadyPromise = null;
        this.initialGlobals = new Set();
        this.onMessageCallback = null;
        this.onErrorCallback = null;
        this.preloadPackages = preloadPackages;
        console.log("Preload packages in WorkerManager:", this.preloadPackages);
        this.initWorker();
        
    }


    initWorker() {
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
                    initialGlobals = new Set(pyodide.globals.keys());
                    postMessage({ type: 'initReady' }); // Notify readiness
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
                        console.log("Loading packages:", packages);
                        await pyodide.loadPackage(packages);
                        console.log("Packages loaded:", packages);
                        postMessage(JSON.stringify({ type: 'packagesLoaded' }));
                    } catch (err) {
                        postMessage(JSON.stringify({ type: 'stderr', msg: String(err)}));
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

    generateInitializationScript(packages) {
        // Start building the initialization script
        let script = `import sys\noriginal_stdout = sys.stdout\nsys.stdout = None\n`;

        // For each package, add a corresponding import statement and a simple usage example to trigger compilation
        packages.forEach(pkg => {
            script += `\nimport ${pkg}\n`;
            if (pkg === 'sympy') {
                script += `from sympy import symbols\nx, y = symbols('x y')\n_ = ${pkg}.solve(x + y - 1, x)\n`;
            } else if (pkg === 'numpy') {
                script += `_ = ${pkg}.zeros((2, 2))\n`;
            } else if (pkg === 'matplotlib') {
                script += `${pkg}.use('Agg')\nimport matplotlib.pyplot as plt\nplt.plot([0, 1], [0, 1])\nplt.close()\n`;
            } else if (pkg === 'scipy') {
                script += `from scipy import optimize\n_ = optimize.minimize(lambda x: x**2, 0)\n`;
            } else {
                // Generic initialization for other packages
                script += `# Simple operation to initialize ${pkg}\n`;
                script += `_ = dir(${pkg})\n`;
            }
        });

        // End of script: restore output
        script += `\nsys.stdout = original_stdout\n`;
        return script;
    }

    runSilentInitialization(initScript) {
        this.worker.postMessage({ type: 'runCode', code: initScript });
    }

    handleMessage(event) {
        let data;
        try {
            data = JSON.parse(event.data);
        } catch (e) {
            data = event.data;
        }

        if (data.type === 'initReady') {
            if (this.preloadPackages && this.preloadPackages.length > 0) {
                // Ensure packages are loaded after worker initialization
                console.log("Preloading packages: ", this.preloadPackages);
                this.loadPackages(this.preloadPackages);
            }
        }
    
        if (this.onMessageCallback) {
            this.onMessageCallback(data);
        }

        // Trigger initialization only after receiving 'packagesLoaded'
        if (data.type === 'packagesLoaded' && !this.isInitialized) {
            console.log("Packages loaded successfully.");
            const initScript = this.generateInitializationScript(this.preloadPackages);
            this.runSilentInitialization(initScript);  // Run only after packages confirm as loaded
            this.isInitialized = true;  // Mark initialization as done
        }
    }

    handleError(error) {
        if (this.onErrorCallback) {
            this.onErrorCallback(error);
        }
    }

    runCode(code) {
        this.worker.postMessage({ type: 'runCode', code });
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

    setMessageCallback(callback) {
        this.onMessageCallback = callback;
    }

    setErrorCallback(callback) {
        this.onErrorCallback = callback;
    }
}