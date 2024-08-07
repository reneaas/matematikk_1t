importScripts('https://cdn.jsdelivr.net/npm/brython@3.10/brython.min.js');

self.onmessage = function(event) {
    const { code, outputId } = event.data;
    
    // Redirect print statements to the main thread
    __BRYTHON__.stdout.write = function(msg) {
        self.postMessage({ type: 'stdout', msg: msg });
    };
    __BRYTHON__.stderr.write = function(msg) {
        self.postMessage({ type: 'stderr', msg: msg });
    };

    // Execute the Python code
    try {
        eval(__BRYTHON__.python_to_js(code));
    } catch (err) {
        self.postMessage({ type: 'stderr', msg: err });
    }

    // Notify completion
    self.postMessage({ type: 'done' });
};

brython();