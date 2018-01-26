#!/bin/bash

# Generates documentation for the functions included in the `functions` directory
# Documentation is generated in Markdown format and placed in the `doc` directory
# GitHub will automatically display this documentation in the repository GitHub pages

# Requires R, Pandoc and rmarkdown


documentation:
	 @for f in functions/*R; do fu="\"$$f"\"; Rscript --slave -e "library('rmarkdown');rmarkdown::render($$fu)"; done
	 cd functions; rm *.html
	 mv functions/*.md docs
