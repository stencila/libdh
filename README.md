# `libdh`


A library of [Stencila](http://stenci.la)-compatible functions for the Digital Humanities.

This library includes functions useful for Digital Humanities data analysis such as:
  - Word Cloud
    - This function generates word clouds for any given group of words. 
  - Collocation (words commonly appearing near each other)
    - Word sets, grouped by cell or by sentence are then combined to create collocations. Words that often appear near each         other will be returned
  - Concordance (the contexts of a given word or set of words)
    - This function returns instances of the sentence or cell that the defined word appears in.
  - N-grams (common two-, three-, etc.- word phrases)
    - Similar to the word cloud function, the n-gram function generates word-cloud images with phrases as opposed to words.
  - Entity recognition (identifying names, places, time periods, etc.)
    - This function is more of a sorting or formatting function. It takes in a list of things and then returns what type of         things they are (i.e. people, places, times, etc).
  - and more.
  
 You are welcome to contribute to the development. 
 
A library of [Stencila](http://stenci.la)-compatible functions for the Digital Humanities. These functions are mostly text-based, charting and categorizing semantic information.


## Testing

The `tests` folder has test files for each function. To run these tests install the [pytest package](https://docs.pytest.org/en/latest/) e.g. `pip install pytest` and then, in the top level folder, run:

```bash
python -m pytest
```
