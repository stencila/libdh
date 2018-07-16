from funcs.collocation import collocation

def test_collocation_string():
    """
    word_cloud can be called with an array of single words (e.g. a column
    of cells containing single words)
    """
    grams = collocation(['nick of time'])
    assert grams == [
        ('of-time', 1),
        ('nick-of', 1),
        ('nick-time', 1)
    ]
def test_collocation_single_words():
    """
    word_cloud can be called with an array of single words (e.g. a column
    of cells containing single words)
    """
    grams = collocation(['time', 'nick of time'])
    assert grams == [
        ('of-time', 1),
        ('nick-of', 1),
        ('nick-time', 1)
    ]

def test_collocation_string_array():
    """
    word_cloud can be called with an array of strings (e.g. a column
    of cells containing strings that aren't limited to one word only)
    """
    grams = collocation(['this is fun', 'nick of time'])
    assert grams == [
        ('this-fun', 1),
        ('this-is', 1),
        ('nick-of', 1),
        ('nick-time', 1),
        ('of-time', 1),
        ('is-fun', 1)
    ]
