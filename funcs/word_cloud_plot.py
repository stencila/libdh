import matplotlib.pyplot as plt
import random

from word_cloud import word_cloud

def word_cloud_plot(values):
    """
    Plot a word cloud

    :param values: Is either a string or an array containing strings
    :return A matplotlib of the actual n gram

    e.g.

       word_cloud_plot(A1:10)
    """

    coords = []
    text_colors = ['red','green','black','blue','purple'] #set list of colors
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
        coords.append([x, x+(width/500), y, y+(height/500)]) #color is randomly selected from list above
    dict = word_cloud(values)
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
