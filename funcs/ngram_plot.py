import matplotlib.pyplot as plt
import numpy as np

from ngram import ngram


def ngram_plot(values, top = 10):
    """
    Plot an ngram

    :param values: Is either a string or an array containing strings
    :param top: Is the number of results you want returned (optional, defaults to 10)
    :return A matplotlib of the actual n gram

    e.g.

       ngram_plot(A1:10)
    """
    dict = ngram(values)

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
