.. meta::
    :description: Execution logging is automatic, just write to STDOUT and Valohai will record everything.

Logging
=======

Everything your commands write to the standard output or standard error streams is logged and visible in real-time
through our command-line client, API and web interface.
That is, you can freely ``print`` things to record anything textual.

**Valohai has a logging limit of 50 messages per second.**
Anything exceeding that will be ignored and you will see a short warning message on your logs.
If you want to record something larger or with faster writing rate,
use :doc:`our outputs system </executions/outputs/index>`.

After your execution has finished, you can download the full log from the web user interface.
Before that, you will be able to inspect last 2000 lines of logs.
