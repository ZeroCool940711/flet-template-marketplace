importScripts("https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js");

self.pythonModuleName = null;
self.initialized = false;
self.flet_js = {}; // namespace for Python global functions

self.initPyodide = async function () {
    self.pyodide = await loadPyodide();
    self.pyodide.registerJsModule("flet_js", flet_js);
    flet_js.documentUrl = documentUrl;
    await self.pyodide.runPythonAsync(`
    from pyodide.http import pyfetch
    response = await pyfetch("assets/app.zip")
    await response.unpack_archive()
  `);
    pyodide.pyimport(self.pythonModuleName);
    await self.flet_js.start_connection(self.receiveCallback);
    self.postMessage("initialized");
};

self.receiveCallback = (message) => {
    self.postMessage(message);
}

self.onmessage = async (event) => {
    // run only once
    if (!self.initialized) {
        self.initialized = true;
        self.documentUrl = event.data.documentUrl;
        self.pythonModuleName = event.data.pythonModuleName;
        await self.initPyodide();
    } else {
        // message
        flet_js.send(event.data);
    }
};