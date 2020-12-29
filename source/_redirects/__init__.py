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
    '/docker-images.html': '/docker-images/',
    '/setup/environments.html': '/setup/environments/',
    '/setup/on-premises/directory-mount.html': '/setup/on-premises/directory-mount/',
    '/setup/on-premises/using-on-premises-workers.html': '/setup/on-premises/using-on-premises-workers/',
    '/setup/on-premises/worker-management.html': '/setup/on-premises/worker-management/',
    '/setup/setup_options.html': '/setup/setup_options/',
    '/core-concepts/notebooks.html': '/core-concepts/notebooks/',
    '/tutorials/apis/downloadMetadata.html': '/tutorials/apis/downloadMetadata/',
    '/tutorials/apis/fetchFailedExecutions.html': '/tutorials/apis/fetchFailedExecutions/',
    '/tutorials/apis/fetchProjects.html': '/tutorials/apis/fetchProjects/',
    '/tutorials/apis/triggerExecFromGitHub.html': '/tutorials/apis/triggerExecFromGitHub/',
    '/valohai-cli/reference/environments.html': '/valohai-cli/reference/environments/',
    '/valohai-cli/reference/execution.html': '/valohai-cli/reference/execution/',
    '/valohai-cli/reference/init.html': '/valohai-cli/reference/init/',
    '/valohai-cli/reference/lint.html': '/valohai-cli/reference/lint/',
    '/valohai-cli/reference/login.html': '/valohai-cli/reference/login',
    '/valohai-cli/reference/logout.html': '/valohai-cli/reference/logout/',
    '/valohai-cli/reference/parcel.html': '/valohai-cli/reference/parcel/',
    '/valohai-cli/reference/project.html': '/valohai-cli/reference/project/',
    '/valohai-cli/reference/update-check.html': '/valohai-cli/reference/update-check/',
    '/valohai-yaml/example-tensorflow-mnist.html': '/valohai-yaml/example-tensorflow-mnist/'
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
        old_path = os.path.join(app.outdir, old.lstrip("/"))
        os.makedirs(os.path.dirname(old_path), exist_ok=True)
        with open(old_path, 'w') as f:
            f.write(TEMPLATE.format(url=new))


def setup(app):
    app.connect('build-finished', install_redirects)
