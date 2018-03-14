import operator
import matplotlib.pyplot as plt
import random
import string
import itertools
import numpy as np

def collocation(cell_list, top = 10):
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
        line = line.split(". ") #split string into sentences
        for sentence in line:
            sentence = sentence.translate(None, string.punctuation) #replace all punctuation
            sentence = sentence.lower() #convert sentence to lower case
            sentence = sentence.split(" ") #split sentence by words
            sentence = list(itertools.combinations(sentence, 2)) #find all 2 word combinations in sentence
            
            #create two versions of the word-pairing, first-second and second-first
            #check for both phrases in the dictionary and update the value of the one that already exists if so
            for i in range(0, len(sentence)):
                phrase = sentence[i][0] + "-" + sentence[i][1]
                phrase1 = sentence[i][1] + "-" + sentence[i][0]
                if phrase in dict:
                    dict[phrase] += 1
                elif phrase1 in dict:
                    dict[phrase1] += 1
                else:
                    dict[phrase] = 1
    dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True) #sort dictionary from most to least frequent

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
        plt.title('Common Collocations')
        top -= 1
        if top == 0:
            break
    return plt
