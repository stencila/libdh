import operator
import matplotlib.pyplot as plt
import random
import string

def word_cloud(cell_list):
    coords = []
    def draw(x, y, fs, col, r):
        global t #allo
        t = plt.text(x, y, key, fontsize=fs,color= col,alpha=alpha_level) #plots text at random position

        #gets information about text box
        bb = t.get_window_extent(renderer=r)
        width = bb.width
        height = bb.height

        #checks to see if current text overlaps other text
        for c in coords:
            #if yes, remove it and try again
            if (((x > c[0] and x < c[1]) or (x + width/500 > c[0] and x + width/500 < c[1])) and ((y > c[2] and y < c[3]) or (y + height/500 > c[2] and y + height/500 < c[3]))):
                t.remove()
                x = random.uniform(0.05, 0.85)
                y = random.uniform(0.05, 0.85)
                draw(x, y, fs, col,r)
        coords.append([x, x+(width/500), y, y+(height/500)]) #coclor is randomly selected from list above

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
    text_colors = ['red','green','black','blue','purple'] #set list of colors

    for line in input: #for each cell, split the string into words by space
        line = line.translate(None, string.punctuation)
        line = line.lower()
        line = line.split(" ")
        for word in line: #add word to dictionary with 1 frequency or add one to frequency of existing word
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True) #sort dictionary from most to least frequent
    max_freq = dict[0][1] #the max_frequency is the value of the first word
    alpha_level = 1

    f = plt.figure()
    r = f.canvas.get_renderer()
    for key, val in dict: #add words to matplotlib at random coordinates with font size relative to max frequency, rotate every other word
        x = random.uniform(0.05, 0.85)
        y = random.uniform(0.05, 0.85)
        fs = (float(val)/max_freq)*40 #scales font size according to relation to maximum frequency
        col = text_colors[random.randint(0,len(text_colors)-1)] #selects random color from color list
        draw(x,y,fs,col,r) #calls draw function to draw text
        alpha_level *= .97 #the transparency level decreases as the word frequency decreases
    plt.axis('off') #removes axes so it's just an image
    return plt
