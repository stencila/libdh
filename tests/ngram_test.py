from funcs.ngram import ngram


def test_ngram_string():
    """
    ngram can be called with a string (e.g. a single cell containing a string)
    """
    grams = ngram('Hello world. Hello, world! Hello Alice and Bob.')
    assert grams == [
        ('world hello', 2),
        ('hello world', 2),
        ('and bob', 1),
        ('hello alice', 1),
        ('alice and', 1)
    ]


def test_ngram_array_string():
    """
    ngram can be called with an array of strings (e.g. a column
    of cells containing strings)
    """
    grams = ngram(['Hello world.', 'Hello, world!', 'Hello... world?'])
    assert grams == [
        ('hello world', 3)
    ]


def test_ngram_single_word():
    """
    ngram will not detect single word phrases
    """
    grams = ngram(['Hello', 'Hello world!', 'world'])
    assert grams == [
        ('hello world', 1)
    ]
