import matplotlib.pyplot as plt

def concordance(cell_list, word):
    input = []
    results = []
    """
    Concordance

    This function generates a concordance graphic based on the strings inputted

    :param cell_list: Is either a string or an array containing strings
    :param word: Is the word that you want to search for
    :return A matplotlib of the actual concordance
    """

    if isinstance(cell_list, str): #if the input is just a string, convert it to a list of one
        input.append(cell_list)
    else:
        input = cell_list

    for line in input: #for each cell, split input into sentences
        line = line.replace('!','.').replace('?','.').split(". ")
        for sentence in line: #plot any sentence that contains keyword in plot
            sentence = sentence.replace(".","")
            if word in sentence.lower():
                results.append(sentence)
    return results
