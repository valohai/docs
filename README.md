# Valohai Platform Documentation

## Development

Setup:

```bash
# Make Python 3 venv for the project if you want to.
pip install -r requirements.txt
yarn  # or npm install
```

Building:

```bash
make watch                # starts 'sphinx-autobuild' server that rebuilds HTML on change, but doesn't watch CSS
make SPHINXOPTS=-E watch  # force regenerates all files
make css                  # converts SCSS to CSS
make html                 # builds the HTML and CSS for distribution
```

## Deployment

Deployment happens automatically when `master` branch updates on GitHub.
