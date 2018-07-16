from funcs.word_cloud import word_cloud

def test_word_cloud_one_word_per_cell():
    """
    word_cloud can be called with an array of single words (e.g. a column
    of cells containing single words)
    """
    grams = word_cloud(['fun', 'yes', 'Fun', 'perfect', 'fun', 'yes'])
    assert grams == [
        ('fun', 3),
        ('yes', 2),
        ('perfect', 1)
    ]

def test_word_cloud_one_string():
    """
    word_cloud can be called with an array of single words (e.g. a column
    of cells containing single words)
    """
    grams = word_cloud(['fun yes Fun perfect fun yes'])
    assert grams == [
        ('fun', 3),
        ('yes', 2),
        ('perfect', 1)
    ]

def test_word_cloud_strings():
    """
    word_cloud can be called with an array of strings (e.g. a column
    of cells containing strings that aren't limited to one word only)
    """
    grams = word_cloud(['this is fun', 'yes we can', 'Fun is good', 'perfect ', 'fun times', 'yes'])
    assert grams == [
        ('fun', 3),
        ('is', 2),
        ('yes', 2),
        ('perfect', 1),
        ('we', 1),
        ('good', 1),
        ('this', 1),
        ('times', 1),
        ('can', 1)
    ]
