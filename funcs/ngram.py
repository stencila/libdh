import operator
import string


def ngram(cell_list, top = 10):
    input = []
    """
    N Gram

    This function generates an n gram graphic based on the strings inputted

    :param cell_list: Is either a string or an array containing strings
    :param top: Is the number of results you want returned (optional, defaults to 10)
    :return: An array of gram, count pairs
    """

    if isinstance(cell_list, str): #if the input is just a string, convert it to a list of one
        input.append(cell_list)
    else:
        input = cell_list

    dict = {} #initialize dictionary

    for line in input: #for each cell, split the string into words by space
        line = line.translate(None, string.punctuation)
        line = line.lower()
        line = line.split(" ")
        for i in range(0, len(line)-1):
            phrase = line[i] + " " + line[i+1]
            if phrase in dict:
                dict[phrase] += 1
            else:
                dict[phrase] = 1
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True) #sort dictionary from most to least frequent
