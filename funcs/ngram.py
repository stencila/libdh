import operator
import matplotlib.pyplot as plt
import random
import string
import numpy as np

def ngram(cell_list, top = 10):
    input = []
    """
    N Gram

    This function generates an n gram graphic based on the strings inputted

    :param cell_list: Is either a string or an array containing strings
    :param top: Is the number of results you want returned (optional, defaults to 10)
    :return A matplotlib of the actual n gram
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
        for i in range(0, len(line)-2):
            phrase = line[i] + " " + line[i+1]
            if phrase in dict:
                dict[phrase] += 1
            else:
                dict[phrase] = 1
    dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True) #sort dictionary from most to least frequent
    alpha_level = 1

    max_freq = dict[0][1] #the max_frequency is the value of the first word
    words = []
    freq = []
    for key, val in dict: #add words to matplotlib at random coordinates with font size relative to max frequency, rotate every other word
        words.append(key)
        y_pos = np.arange(len(words))
        freq.append(val)

        plt.bar(y_pos, freq, align='center')
        plt.xticks(y_pos, words)
        plt.ylabel('Frequency')
        plt.title('Common Ngrams')
        top -= 1
        if top == 0:
            break
    return plt
