# vscode-unittest-failure

This repo was created for two issues raised on the /microsoft/vscode-python/ repo. Thanks in advance to @karthiknadig and any others for the help.

* https://github.com/microsoft/vscode-python/issues/17523
* ~~https://github.com/microsoft/vscode-python/issues/17386~~ (Resolved)


## Steps to reproduce

* Build and open in container on a Linux OS
* Open Output panel, and choose Python from drop down to see stack trace failing to find location

```
User belongs to experiment group 'pythonaacf'
User belongs to experiment group 'pythonJediLSP'
User belongs to experiment group 'pythonDiscoveryModuleWithoutWatcher'
User belongs to experiment group 'pythonTensorboardExperiment'
User belongs to experiment group 'PythonPyTorchProfiler'
User belongs to experiment group 'pythonDeprecatePythonPath'
User belongs to experiment group 'pythonSortEnvs'
User belongs to experiment group 'pythonRunFailedTestsButtonDisplayedcf'
User belongs to experiment group 'pythonRefreshTestsButtonDisplayed'
User belongs to experiment group 'pythonRememberDebugConfig'
Python interpreter path: /usr/local/bin/python
Starting Pylance language server.
Error 2021-09-25 05:22:43: Failed to check if file needs to be fixed [EntryNotFound (FileSystemError): Unable to read file 'vscode-remote://dev-container+2f686f6d652f6368656573653835322f446f63756d656e74732f4769744875622f6b6564796f75/root/.config/Code/User/settings.json' (Error: Unable to resolve non-existing file 'vscode-remote://dev-container+2f686f6d652f6368656573653835322f446f63756d656e74732f4769744875622f6b6564796f75/root/.config/Code/User/settings.json')
	at _handleError (/root/.vscode-server/bin/7f6ab5485bbc008386c4386d08766667e155244e/out/vs/server/remoteExtensionHostProcess.js:94:160087)
	at processTicksAndRejections (internal/process/task_queues.js:93:5)
	at async y.readText (/root/.vscode-server/extensions/ms-python.python-2021.9.1246542782/out/client/extension.js:9:314351)
	at async p.doesFileNeedToBeFixed (/root/.vscode-server/extensions/ms-python.python-2021.9.1246542782/out/client/extension.js:59:823969)
	at async /root/.vscode-server/extensions/ms-python.python-2021.9.1246542782/out/client/extension.js:59:823096
	at async Promise.all (index 0)
	at async p.getFilesToBeFixed (/root/.vscode-server/extensions/ms-python.python-2021.9.1246542782/out/client/extension.js:59:823042)
	at async p.updateTestSettings (/root/.vscode-server/extensions/ms-python.python-2021.9.1246542782/out/client/extension.js:59:822669)] {
  code: 'FileNotFound'
}
> conda --version
```
