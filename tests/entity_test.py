from funcs.entity_recognition import entity_recognition

def test_entity_recognition_array_places():
    """
    entity_recognition can be called with an array of strings (e.g. a column
    of cells containing strings)
    """
    grams = entity_recognition(['Germany', 'France', '154', 'New Zealand'])
    assert grams == 'GPE'

def test_entity_recognition_array_people():
    """
    entity_recognition can be called with an array of strings (e.g. a column
    of cells containing strings)
    """
    grams = entity_recognition(['Barack Obama', 'Mark Wahlber', 'Notes', 'Elon Musk'])
    assert grams == 'PERSON'
