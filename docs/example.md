---
title: Sample HTML report generated from R script
author: Andrew Brooks
date: March 4, 2015
output:
 html_document:
  keep_md: true
  self_contained: true
---
## Generate document body from comments
All the features from markdown and markdown supported within .Rmd documents, I was able to
get from within R scripts.  Here are some that I tested and use most frequently:

* Smart comment fomatting in your R script generate the body and headers of the document
    * Simply tweak your comments to begin with `#'` instead of just `#`
* Create markdown headers as normal: `#' #` for h1, `#' ##` for h2, etc.
* Add two spaces to the end of a comment line to start a new line (just like regular markdown)
* Add `toc: true` to YAML frontmatter to create a table of contents with links like the one at the
top of this page that links to h1, h2 & h3's indented like so:
    * h1
        * h2
            * h3
* Modify YAML to change syntax highlighting style (I'm using zenburn), author, title, theme, and all the good stuff
you're used to setting in Rmd documents.
* Sub-bullets like the ones above are created by a `#' *` with 4 spaces per level of indentation.
* Surround text with `*` to *italicize*
* Surround text with `**` to **bold**
* Surround text with `***` to ***italicize & bold***
* Skip lines with `#' <br>`
* Keep comments in code, but hide from printing in report with `#' <!-- this text will not print in report -->`
* Add hyperlinks:
    * [Rmarkdown cheatsheet](http://rmarkdown.rstudio.com/RMarkdownCheatSheet.pdf)
    * [Rmarkdown Reference Guide](http://rmarkdown.rstudio.com/RMarkdownReferenceGuide.pdf)
    * [Compiling R notebooks from R Scripts](http://rmarkdown.rstudio.com/r_notebook_format.html)



```r
# comments without the extra tick show up like this.  And get included in code blocks
# loading mtcars data
data(mtcars)
```

## Messing with data


```r
library('knitr')
```

### 3 ways to print an object
...specifically a data.frame in this case.  Ordered from least to most pretty (in my opinion).


```r
print(head(mtcars))
```

```
##                    mpg cyl disp  hp drat    wt  qsec vs am gear carb
## Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
## Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
## Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
## Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
## Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
## Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1
```

```r
knitr::kable(head(mtcars))
```

                      mpg   cyl   disp    hp   drat      wt    qsec   vs   am   gear   carb
------------------  -----  ----  -----  ----  -----  ------  ------  ---  ---  -----  -----
Mazda RX4            21.0     6    160   110   3.90   2.620   16.46    0    1      4      4
Mazda RX4 Wag        21.0     6    160   110   3.90   2.875   17.02    0    1      4      4
Datsun 710           22.8     4    108    93   3.85   2.320   18.61    1    1      4      1
Hornet 4 Drive       21.4     6    258   110   3.08   3.215   19.44    1    0      3      1
Hornet Sportabout    18.7     8    360   175   3.15   3.440   17.02    0    0      3      2
Valiant              18.1     6    225   105   2.76   3.460   20.22    1    0      3      1

including `#+ results='asis'` chunk option for formatting


```r
knitr::kable(head(mtcars))
```

                      mpg   cyl   disp    hp   drat      wt    qsec   vs   am   gear   carb
------------------  -----  ----  -----  ----  -----  ------  ------  ---  ---  -----  -----
Mazda RX4            21.0     6    160   110   3.90   2.620   16.46    0    1      4      4
Mazda RX4 Wag        21.0     6    160   110   3.90   2.875   17.02    0    1      4      4
Datsun 710           22.8     4    108    93   3.85   2.320   18.61    1    1      4      1
Hornet 4 Drive       21.4     6    258   110   3.08   3.215   19.44    1    0      3      1
Hornet Sportabout    18.7     8    360   175   3.15   3.440   17.02    0    0      3      2
Valiant              18.1     6    225   105   2.76   3.460   20.22    1    0      3      1

### Plotting


```r
plot(mtcars$mpg, mtcars$disp, col=mtcars$cyl, pch=19)
```

![](example_files/figure-html/unnamed-chunk-5-1.png)<!-- -->

We can change the chunk options we would use for a code block using `knitr` by using a comment that starts with `#+`.
For example, to change the plot size, we can specify `#+ fig.width=4, fig.height=4` before plotting.
<br>
A new chunk is automatically generated (chunk settings reset) whenever we add document text with `#'` or change.
However, it is possible to specify global chunk options, if desired.
chunk options again with `#+`.

---
title: "example.R"
author: "aleksandra"
date: "Fri Jan 26 22:11:07 2018"
---
