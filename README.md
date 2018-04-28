# `libdh`


A library of [Stencila](http://stenci.la)-compatible functions for the Digital Humanities.

This library includes functions useful for Digital Humanities data analysis such as:
  - Word Cloud
  - Collocation (words commonly appearing near each other)
  - Concordance (the contexts of a given word or set of words)
  - N-grams (common two-, three-, etc.- word phrases)
  - Entity recognition (identifying names, places, time periods, etc.)
  - and more.
  
 You are welcome to contribute to the development. 
 
A library of [Stencila](http://stenci.la)-compatible functions for the Digital Humanities. These functions are mostly text-based, charting and categorizing semantic information.


## Testing

The `tests` folder has test files for each function. To run these tests install the [pytest package](https://docs.pytest.org/en/latest/) e.g. `pip install pytest` and then, in the top level folder, run:

```bash
python -m pytest
```
