After you start the execution, you are forwarded to the execution page.

This page has several tabs with execution details:

The **Information** tab shows the basic information about the execution, most of which could've been modified in
the previous execution creation step.

The **Log** tab shows real-time log output from the execution.
Anything that your code prints to the standard output (stdout) or standard error (stderr) streams is shown here.

The **Metadata** tab shows all the metadata output from the execution.
You can also plot the metadata on a line chart.
Metadata is any data your execution writes to the standard output stream in JSON which we can parse.
If no plottable metadata has been output, this tab is not visible.

The **Output** tab contains download links for all the output artifacts created by the execution.
The execution defines these outputs by writing them into ``/valohai/outputs`` directory.
The artifacts are stored in AWS S3.
If the execution has not finished, or did not output any files, this tab will not be visible.
