# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command-line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = Valohai
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile check-descriptions
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

check-descriptions:
	python check_descriptions.py

watch: check-descriptions
	sphinx-autobuild -b dirhtml --port 44044 "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
