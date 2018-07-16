import matplotlib.pyplot as plt
import numpy as np
from collocation import collocation

def collocation_plot(values, top = 10):
    """
    Plot a collocation

    :param values: Is either a string or an array containing strings
    :param top: Is the number of results you want returned (optional, defaults to 10)
    :return A matplotlib of the actual collocations

    e.g.

       collocation_plot(A1:10)
    """

    dict = collocation(values, top)
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
