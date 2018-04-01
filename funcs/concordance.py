import operator
import matplotlib.pyplot as plt
import random
import string
import itertools
import numpy as np

def collocation(cell_list, word):
    input = []
    """
    N Gram

    This function generates an n gram graphic based on the strings inputted

    :param cell_list: Is either a string or an array containing strings
    :param word: Is the word that you want to search for
    :return A matplotlib of the actual n gram
    """

    if isinstance(cell_list, str): #if the input is just a string, convert it to a list of one
        input.append(cell_list)
    else:
        input = cell_list

    dict = {} #initialize dictionary

    for line in input: #for each cell, split input into sentences
        line = line.split(". ")
        y_val = 1 #initialize y axis values
        for sentence in line: #plot any sentence that contains keyword in plot
            if word in sentence.lower():
                plt.text(0, y_val, sentence)
                y_val -= .05
    plt.axis('off') #removes axes so it's just an image
    return plt
