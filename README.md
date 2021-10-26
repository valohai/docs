# Valohai Platform Documentation

## Development

Setup:

```bash
# Make Python 3 venv for the project if you want to.
pip install -r requirements.txt
```

Building:

```bash
make watch                # starts development server that rebuilds HTML on change
make SPHINXOPTS=-E watch  # ... also force regenerates all files on server start
make dirhtml              # builds the HTML for distribution
```

## Deployment

Deployment happens automatically when `master` branch updates on GitHub.
