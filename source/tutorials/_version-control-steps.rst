A valid source repository must contain a ``valohai.yaml`` configuration file that defines how workers will run your machine learning code. All of our examples have that defined already.

Let's set up a repository for your project:

1. Go to the example repository page on GitHub:

  * |example-repository-url|
  * If you want to modify the training code, you can fork the repository first.

2. Copy the **HTTPS** URL of the repository:

  * |example-repository-url|.git
  * Using an SSH URLs work only for private GitHub repositories.

3. Go to the **Repository** tab inside your new project to set your source repository
4. Paste the URL above to the ``URL`` field on the **Repository** tab
5. Leave ``Fetch reference`` as the default value `master`
6. ``SSH private key`` is only required if your Git repository is private
7. Press the **Save** button
