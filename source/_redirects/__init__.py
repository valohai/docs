import os

# Allows creating JS-based redirect pages.
# Required as the docs are hosted as a static website.

redirects = {
    # '/old-page/index.html': '/new-page/awesome/whatever.html'

    # moving some core concepts to be under Execution details
    '/core-concepts/live-upload.html': '/executions/live-outputs/',
    '/core-concepts/metadata.html': '/executions/metadata/',

    # single file HTML builder to directory builder change...
    '/quickstarts/quick-start-tensorflow.html': '/quickstarts/quick-start-tensorflow/',
    '/quickstarts/quick-start-keras.html': '/quickstarts/quick-start-keras/',
    '/quickstarts/quick-start-r.html': '/quickstarts/quick-start-r/',
    '/quickstarts/quick-start-cli.html': '/quickstarts/quick-start-cli/',
    '/quickstarts/quick-start-api.html': '/quickstarts/quick-start-api/',
    '/core-concepts/what-is-valohai.html': '/core-concepts/what-is-valohai/',
    '/core-concepts/projects.html': '/core-concepts/projects/',
    '/core-concepts/configuration-file.html': '/core-concepts/configuration-file/',
    '/core-concepts/steps.html': '/core-concepts/steps/',
    '/core-concepts/executions.html': '/core-concepts/executions/',
    '/core-concepts/parameters.html': '/core-concepts/parameters/',
    '/core-concepts/data-stores.html': '/core-concepts/data-stores/',
    '/core-concepts/tasks.html': '/core-concepts/tasks/',
    '/core-concepts/pipelines.html': '/core-concepts/pipelines/',
    '/core-concepts/deployments.html': '/core-concepts/deployments/',
    '/valohai-yaml/step.html': '/valohai-yaml/step/',
    '/valohai-yaml/step-name.html': '/valohai-yaml/step-name/',
    '/valohai-yaml/step-image.html': '/valohai-yaml/step-image/',
    '/valohai-yaml/step-command.html': '/valohai-yaml/step-command/',
    '/valohai-yaml/step-parameters.html': '/valohai-yaml/step-parameters/',
    '/valohai-yaml/step-inputs.html': '/valohai-yaml/step-inputs/',
    '/valohai-yaml/step-environment.html': '/valohai-yaml/step-environment/',
    '/valohai-yaml/step-environment-variables.html': '/valohai-yaml/step-environment-variables/',
    '/valohai-yaml/endpoint.html': '/valohai-yaml/endpoint/',
    '/valohai-cli/installation.html': '/valohai-cli/installation/',
    '/valohai-cli/using-inputs.html': '/valohai-cli/using-inputs/',
    '/valohai-cli/using-environments.html': '/valohai-cli/using-environments/',
    '/on-premises/directory-mount.html': '/on-premises/directory-mount/',
    '/on-premises/using-on-premises-workers.html': '/on-premises/using-on-premises-workers/',
    '/on-premises/worker-management.html': '/on-premises/worker-management/',
}

TEMPLATE = """
<html>
  <head>
    <meta http-equiv="refresh" content="1; url={url}:" />
    <script>
      window.location.href = "{url}"
    </script>
  </head>
</html>
"""


def install_redirects(app, exception):
    """
    Save JS redirect pages according to the source => destination
    mapping in the "redirects" dictionary.
    """
    for old, new in redirects.items():
        old_path = app.outdir.rstrip('/') + '/' + old.lstrip('/')

        if os.path.isfile(old_path):
            # redirecting overwrite all other files
            os.remove(old_path)

        with open(old_path, 'w+') as f:
            f.write(TEMPLATE.format(url=new))


def setup(app):
    app.connect('build-finished', install_redirects)
