import os

# Allows creating JS-based redirect pages.
# Required as the docs are hosted as a static website.

redirects = {
    # '/old-page/index.html': '/new-page/awesome/whatever.html'
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
