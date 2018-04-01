from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree

def entity_recognition(cell_list):
    input = []
    nodes = []
    results = []
    """
    Entity Recognition

    This function returns the entity type of the column inputted

    :param cell_list: Is either a string or an array containing strings
    :return The entity type of the column
    """

    if isinstance(cell_list, str): #if the input is just a string, convert it to a list of one
        input.append(cell_list)
    else:
        input = cell_list

    #tags each cell as an entity (if possible) then gets and returns the most common one
    for line in input:
        node = pos_tag(word_tokenize(line))
        node = ne_chunk(node)
        for elt in node:
            if isinstance(elt, Tree):
                nodes.append(Tree(elt.label(), [ word for word, tag in elt ]))
    for n in nodes:
        results.append(n.label())

    return max(set(results), key=results.count)
