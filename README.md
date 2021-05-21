# Valohai Platform Documentation

## Development

Setup:

```bash
# Make Python 3 venv for the project if you want to.
pip install -r requirements.txt
```

Building:

```bash
make watch                # starts 'sphinx-autobuild' server that rebuilds HTML on change, but doesn't watch CSS
make SPHINXOPTS=-E watch  # force regenerates all files
make html                 # builds the HTML for distribution
```

## Deployment

Deployment happens automatically when `master` branch updates on GitHub.
