import matplotlib.pyplot as plt
from concordance import concordance

def concordance_plot(values, word):
    """
    Plot a concordance

    :param values: Is either a string or an array containing strings
    :param word: Is the word that is being searched for
    :return A matplotlib of the actual concordances

    e.g.

       concordance_plot(A1:10)
    """
    sentences = concordance(values, word)
    y_val = 1 #initialize y axis values
    for s in sentences: #plot any sentence that contains keyword in plot
        plt.text(0, y_val, s)
        y_val -= .05
    plt.axis('off') #removes axes so it's just an image
    return plt
