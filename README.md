# vscode-unittest-failure

Created for an issue raised on the /microsoft/vscode-python/ repo. Thanks in advance to @karthiknadig and any others for the help.

https://github.com/microsoft/vscode-python/issues/17386

## Steps to reproduce

* Open this repo as a dev container
* This repo has two tests in the `test.py` file. When the tests are ran from the terminal with `python manage.py test`, the output successfully runs as follows:

```
vscode ➜ /workspace (main) $ cd mysite/
vscode ➜ /workspace/mysite (main) $ python manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F.
======================================================================
FAIL: test_that_should_fail (mysite.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/mysite/mysite/tests.py", line 7, in test_that_should_fail
    self.assertIs(True, False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

* The above results are expected to be also visible in the Testing panel of VS Code using the python extension.
* However, the tests fail to produce a visible output, and the VS Code developer tools show the following error message:

```
[[object Object]]Maximum call stack size exceeded
$onExtensionRuntimeError @ workbench.desktop.main.js:1992
_doInvokeHandler @ workbench.desktop.main.js:1502
_invokeHandler @ workbench.desktop.main.js:1502
_receiveRequest @ workbench.desktop.main.js:1502
_receiveOneMessage @ workbench.desktop.main.js:1502
(anonymous) @ workbench.desktop.main.js:1502
fire @ workbench.desktop.main.js:69
fire @ workbench.desktop.main.js:85
_receiveMessage @ workbench.desktop.main.js:85
(anonymous) @ workbench.desktop.main.js:85
fire @ workbench.desktop.main.js:69
acceptChunk @ workbench.desktop.main.js:85
(anonymous) @ workbench.desktop.main.js:85
(anonymous) @ workbench.desktop.main.js:609
fire @ workbench.desktop.main.js:69
E._fileReader.onload @ workbench.desktop.main.js:609
load (async)
E @ workbench.desktop.main.js:609
create @ workbench.desktop.main.js:609
connect @ workbench.desktop.main.js:609
a @ workbench.desktop.main.js:609
n @ workbench.desktop.main.js:609
s @ workbench.desktop.main.js:609
f @ workbench.desktop.main.js:609
m @ workbench.desktop.main.js:609
processTicksAndRejections @ internal/process/task_queues.js:93
async function (async)
m @ workbench.desktop.main.js:609
(anonymous) @ workbench.desktop.main.js:1543
processTicksAndRejections @ internal/process/task_queues.js:93
Promise.then (async)
start @ workbench.desktop.main.js:1543
Cr @ workbench.desktop.main.js:1537
_createInstance @ workbench.desktop.main.js:600
createInstance @ workbench.desktop.main.js:600
i @ workbench.desktop.main.js:1537
(anonymous) @ workbench.desktop.main.js:2872
_startExtensionHosts @ workbench.desktop.main.js:2872
_initialize @ workbench.desktop.main.js:2872
(anonymous) @ workbench.desktop.main.js:2878
requestIdleCallback (async)
e.runWhenIdle @ workbench.desktop.main.js:77
(anonymous) @ workbench.desktop.main.js:2878
Promise.then (async)
cl @ workbench.desktop.main.js:2878
_createInstance @ workbench.desktop.main.js:600
_createServiceInstance @ workbench.desktop.main.js:600
_createServiceInstanceWithOwner @ workbench.desktop.main.js:600
_createAndCacheServiceInstance @ workbench.desktop.main.js:600
_safeCreateAndCacheServiceInstance @ workbench.desktop.main.js:600
_getOrCreateServiceInstance @ workbench.desktop.main.js:600
get @ workbench.desktop.main.js:600
initLayout @ workbench.desktop.main.js:2641
(anonymous) @ workbench.desktop.main.js:2641
invokeFunction @ workbench.desktop.main.js:600
startup @ workbench.desktop.main.js:2641
open @ workbench.desktop.main.js:2790
async function (async)
open @ workbench.desktop.main.js:2790
w @ workbench.desktop.main.js:2790
m.load.configureDeveloperSettings @ workbench.js:32
(anonymous) @ bootstrap-window.js:171
r._invokeFactory @ loader.js:1136
r.complete @ loader.js:1146
r._onModuleComplete @ loader.js:1772
r._onModuleComplete @ loader.js:1784
r._resolve @ loader.js:1732
r.defineModule @ loader.js:1375
p @ loader.js:1822
define @ loader.js:1900
(anonymous) @ workbench.desktop.main.js:2878
(anonymous) @ workbench.desktop.main.js:2878
```
