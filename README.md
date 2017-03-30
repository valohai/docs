# Valohai Platform Documentation

## Development

* `make watch` will open a [`sphinx-autobuild`](sab) server for you.
  It automagically rebuilds documentation.
* `make html` will build the HTML documentation for distribution.

### Style development 

* `make css` will convert SCSS to CSS.
* When developing styles, use `make SPHINXOPTS=-E watch` to have Sphinx regenerate all files.
