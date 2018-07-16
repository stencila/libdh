import operator
import matplotlib.pyplot as plt
import string

def word_cloud(cell_list):

    input = []

    """
    Word Cloud

    This function generates a word cloud graphic based on the strings inputted

    :param cell_list: Is either a string or an array containing strings
    :return A matplotlib of the actual word cloud
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
        for word in line: #add word to dictionary with 1 frequency or add one to frequency of existing word
            if word != '': #gets rid of spaces at end of sentences
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True) #sort dictionary from most to least frequent
