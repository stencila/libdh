from funcs.concordance import concordance


def test_concordance_string():
    """
    concordance can be called with a string (e.g. a single cell containing a string)
    """
    grams = concordance('Hello world. Hello, my great world! Hello Alice and Bob.', 'world')
    assert grams == [
        ('Hello world'),
        ('Hello, my great world')
    ]

def test_concordance_array_string():
    """
    concordance can be called with an array of strings (e.g. a column
    of cells containing strings)
    """
    grams = concordance(['Hello world.', 'Hello, my great world!', 'Hello Alice and Bob.'], 'world')
    assert grams == [
        ('Hello world'),
        ('Hello, my great world')
    ]
