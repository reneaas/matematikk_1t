const CACHE_NAME = 'pyodide-cache';
const urlsToCache = [
    'https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js',
    'https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.asm.wasm',
    // Add other necessary files
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});