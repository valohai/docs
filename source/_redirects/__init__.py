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
    '/setup/setup-options.html': '/setup/setup-options/',
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
    '/valohai-yaml/example-tensorflow-mnist.html': '/valohai-yaml/example-tensorflow-mnist/',


    # '/old-page/index.html': '/new-page/awesome/whatever.html'
    '/tutorials/accessing-repositories-during-executions/index.html': '/howto/code-repository/accessing-repositories-during-executions/index.html',
    '/tutorials/azure-ad/index.html': '/howto/organization/azure-ad/index.html',
    '/tutorials/build-docker-image/index.html': '/tutorials/docker-build-image.html',
    '/tutorials/build-docker-image/index.html': '/tutorials/docker-build-image.html',
    '/tutorials/cloud-storage/index.html': '/howto/data/cloud-storage/index.html',
    '/tutorials/cloud-storage/private-azure-storage/index.html': '/howto/data/cloud-storage/private-azure-storage/index.html',
    '/tutorials/cloud-storage/private-gcp-bucket/index.html': '/howto/data/cloud-storage/private-gcp-bucket/index.html',
    '/tutorials/cloud-storage/private-s3-bucket/index.html': '/howto/data/cloud-storage/private-s3-bucket/index.html',
    '/tutorials/cloud-storage/private-swift-container/index.html': '/howto/data/cloud-storage/private-swift-container/index.html',
    '/tutorials/code-repository/index.html': '/howto/code-repository/index.html',
    '/tutorials/code-repository/private-gitlab-repository/index.html': '/howto/code-repository/private-gitlab-repository/index.html',
    '/tutorials/code-repository/private-gitlab-repository/': '/howto/code-repository/private-gitlab-repository/',
    '/tutorials/code-repository/private-bitbucket-repository/index.html': '/howto/code-repository/private-bitbucket-repository/index.html',
    '/tutorials/code-repository/private-bitbucket-repository/': '/howto/code-repository/private-bitbucket-repository/',
    '/tutorials/code-repository/private-github-repository/index.html': '/howto/code-repository/private-github-repository/index.html',
    '/tutorials/code-repository/private-github-repository/': '/howto/code-repository/private-github-repository/',
    '/tutorials/valohai/index.html': '/tutorials/quickstart/index.html',
    '/tutorials/valohai/advanced/': '/tutorials/quickstart/',
    '/tutorials/valohai/onboard-team/index.html': '/howto/organization/',
    '/tutorials/valohai/onboard-team/index.html': '/howto/organization/',
    '/valohai-yaml/': '/reference-guides/valohai-yaml/',
    '/valohai-yaml/step.html': '/reference-guides/valohai-yaml/step.html',
    '/valohai-yaml/step-parameters.html': '/reference-guides/valohai-yaml/step-parameters.html',
    '/valohai-yaml/step-name.html': '/reference-guides/valohai-yaml/step-name.html',
    '/valohai-yaml/step-inputs.html': '/reference-guides/valohai-yaml/step-inputs.html',
    '/valohai-yaml/step-image.html': '/reference-guides/valohai-yaml/step-image.html',
    '/valohai-yaml/step-environment.html': '/reference-guides/valohai-yaml/step-environment.html',
    '/valohai-yaml/step-environment-variables.html': '/reference-guides/valohai-yaml/step-environment-variables.html',
    '/valohai-yaml/step-command.html': '/reference-guides/valohai-yaml/step-command.html',
    '/valohai-yaml/example-tensorflow-mnist.html': '/reference-guides/valohai-yaml/example-tensorflow-mnist.html',
    '/valohai-yaml/environment-variables-project.html': '/reference-guides/valohai-yaml/environment-variables-project.html',
    '/valohai-yaml/environment-variables-execution.html': '/reference-guides/valohai-yaml/environment-variables-execution.html',
    '/valohai-yaml/pipeline/': '/reference-guides/valohai-yaml/pipeline/',
    '/valohai-yaml/pipeline/nodes/': '/reference-guides/valohai-yaml/pipeline/nodes/',
    '/valohai-yaml/pipeline/edges/': '/reference-guides/valohai-yaml/pipeline/edges/',
    '/valohai-yaml/endpoint/': '/reference-guides/valohai-yaml/endpoint/',
    '/valohai-yaml/endpoint/wsgi/': '/reference-guides/valohai-yaml/endpoint/wsgi/',
    '/valohai-yaml/endpoint/server-command/': '/reference-guides/valohai-yaml/endpoint/server-command/',
    '/setup/': '/topic-guides/setup/',
    '/setup/onboarding.html': '/topic-guides/setup/onboarding.html',
    '/setup/setup-options.html': '/topic-guides/setup/setup-options.html',
    '/setup/environments.html': '/topic-guides/setup/environments.html',
    '/setup/on-premises/': '/topic-guides/setup/on-premises/',
    '/setup/on-premises/directory-mount.html': '/topic-guides/setup/on-premises/directory-mount.html',
    '/setup/on-premises/using-on-premises-workers.html': '/topic-guides/setup/on-premises/using-on-premises-workers.html',
    '/setup/on-premises/worker-management.html': '/topic-guides/setup/on-premises/worker-management.html',
    '/quickstarts/': '/tutorials/example-project/',
    '/quickstarts/quick-start-api.html': '/tutorials/example-project/quick-start-api.html',
    '/quickstarts/quick-start-cli.html': '/tutorials/example-project/quick-start-cli.html',
    '/quickstarts/quick-start-keras.html': '/tutorials/example-project/quick-start-keras.html',
    '/quickstarts/quick-start-r.html': '/tutorials/example-project/quick-start-r.html',
    '/quickstarts/quick-start-tensorflow.html': '/tutorials/example-project/quick-start-tensorflow.html',
    '/quickstarts/quick-start-jupyter/': '/tutorials/jupyter/jupyhai/',
    '/quickstarts/quick-start-jupyter/hosted/': '/tutorials/jupyter/jupyhai/',
    '/quickstarts/quick-start-jupyter/jupyhai/': '/tutorials/jupyter/jupyhai/',
    '/jupyter/': '/tutorials/jupyter/jupyhai/',
    '/executions/': '/topic-guides/executions/',
    '/executions/envvar-config/': '/topic-guides/executions/envvar-config/',
    '/executions/file-config/': '/topic-guides/executions/file-config/',
    '/executions/inputs/': '/topic-guides/executions/inputs/',
    '/executions/lifecycle/': '/topic-guides/executions/lifecycle/',
    '/executions/live-outputs/': '/topic-guides/executions/live-outputs/',
    '/executions/logs/': '/topic-guides/executions/logs/',
    '/executions/metadata/': '/topic-guides/executions/metadata/',
    '/executions/outputs/': '/topic-guides/executions/outputs/',
    '/executions/placeholder-config/': '/topic-guides/executions/placeholder-config/',
    '/core-concepts/': '/topic-guides/core-concepts/',
    '/core-concepts/configuration-file.html': '/topic-guides/core-concepts//configuration-file.html',
    '/core-concepts/data-stores.html': '/topic-guides/core-concepts/data-stores.html',
    '/core-concepts/deployments.html': '/topic-guides/core-concepts/deployments.html',
    '/core-concepts/executions.html': '/topic-guides/core-concepts/executions.html',
    '/core-concepts/notebooks.html': '/topic-guides/core-concepts/notebooks.html',
    '/core-concepts/parameters.html': '/topic-guides/core-concepts/parameters.html',
    '/core-concepts/pipelines.html': '/topic-guides/core-concepts/pipelines.html',
    '/core-concepts/projects.html': '/topic-guides/core-concepts/projects.html',
    '/core-concepts/steps.html': '/topic-guides/core-concepts/steps.html',
    '/core-concepts/tasks.html': '/topic-guides/core-concepts/tasks.html',
    '/core-concepts/what-is-valohai.html': '/topic-guides/core-concepts/',
    '/architecture/': '/topic-guides/architecture/',
    '/docker-images.html': '/topic-guides/docker-images/',
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
