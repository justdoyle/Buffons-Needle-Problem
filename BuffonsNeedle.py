import numpy as np #import necessary packages
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
import math
from math import sin, cos, tan
import random
rng = np.random.default_rng() #for generating throwing of needles

root = tk.Tk(screenName = "Buffon's Needle Problem") #start tkinter window app
root.geometry("1000x500") #set window size


titlelab = tk.Label(root, text = "This Program is Designed to Estimate pi Using Buffon's Needle Problem") #set preliminary title
titlelab.pack() #place title in window
canvas = None #prep empty canvas


def getchart(): #function to generate the buffons needle problem diagram after function called from button press
    global titlelab, canvas #take global values for variables so we can reset them
    titlelab.destroy() #remove title label to make room for new one
    if canvas is not None:
        canvas.get_tk_widget().destroy() #remove canvas to make room for new one
    plt.close('all') #close all plots to allow for new plots to be made
    lineamt = sliders["Number of Lines"].get() #retrieve the values associated with the corresponding sliders
    needamt = sliders["Number of Needles"].get()
    needleng = sliders["Length of Needles"].get()
    linespac = sliders["Space Between Lines"].get()
    linelen = sliders["Length of Lines"].get()

    print(str(lineamt) + ' Lines, ' + str(needamt) + ' Needles, ' + str(needleng) + ' Needle Length and ' + str(linespac) + ' Line Space \n') #print the variales of the graph currently getting retrieved to show request gone through

    linefirst = linespac / 2 #set variable for line positioning of first line
    linelast =  (linespac / 2) + ((lineamt - 1)*linespac) #set variable for line positioning of last line
    linesetup = np.linspace(linefirst, linelast, lineamt) #set up lines to be thrown on to
    xlimit = linelast + (linespac / 2) #set axis limits for needles and producing figure
    ylimit = linelen 

    randstarx = rng.uniform(low = 0, high = xlimit, size = needamt) #give random start positions of needles x
    randstary = rng.uniform(low = 0, high = ylimit, size = needamt) #and y
    randang = rng.uniform(low = 0 , high = 2 * math.pi  , size = needamt) #give random angles of needles

    randendx = np.empty(needamt) #set up empty arrays to fill with end points of the needles
    randendy = np.empty(needamt)
    widthfig = 8 #set base width of plot to produce in window
    heightfig = widthfig * (ylimit/xlimit) #calculate the corresponding height based on the variables
    if heightfig > 3: #to stop from exceeding space for canvas
        heightfig = 3
        widthfig = heightfig * (xlimit/ylimit)
    fig = Figure(figsize = (widthfig , heightfig)) #prepare figure for plotting onto
    axes = fig.add_subplot(111) #prepare subplot such that we can manipulate plot elements
    axes.vlines(linesetup, 0 , ylimit , linestyles = 'solid' , colors = 'r') #plot vertical lines on plot
    for endcalc in range(needamt): #for all needles
        randendx[endcalc] = randstarx[endcalc] + (needleng * cos(randang[endcalc])) #calculate end x and y point of the needles given the start points and angles
        randendy[endcalc] = randstary[endcalc] + (needleng * sin(randang[endcalc]))

        axes.plot([randstarx[endcalc],randendx[endcalc]],[randstary[endcalc],randendy[endcalc]], linewidth = '0.5') #plot each needle as line on chart

    buffcount = 0 #initialise counter for needles on lines
    for hitline in linesetup: #for each line
        for buffcheck in range(needamt): #for each needle
            if randstarx[buffcheck] <= hitline <= randendx[buffcheck] or randstarx[buffcheck] >= hitline >= randendx[buffcheck]: #check if needle coords go over a line
                buffcount += 1 #add to counter if they do

    if buffcount != 0:
        piest = ((2 * needamt) * needleng) / (buffcount * linespac) #calculate the pi estimation based on the number of needles thrown and the number of needles that land on a line
    else:
        piest = 'None Landed On Lines'

    axes.set_position([0, 0, 1, 1]) #sets range of plot to remove excess whitespace when axes have gone
    axes.set_aspect('equal') #ensure the axes are equally scaled
    axes.set_xlim(0,xlimit) #set range for axes
    axes.set_ylim(0,ylimit)
    axes.axis('off') #removes axis from plot to leave only the image of the plotted lines

    canvas = FigureCanvasTkAgg(fig, master = root) #prep a matplotlib canvas for the figure created
    canvas.draw() #create the physical object of the figure
    canvas.get_tk_widget().place(x = 550, y = 180, anchor = 'center') #place the canvas of the plot onto the window

    titlelab = tk.Label(root , text = (str(lineamt) + ' Lines, ' + str(needamt) + ' Needles, ' + str(needleng) + ' Needle Length and ' + str(linespac) + ' Line Space \n' + #preparing title
    str(buffcount) + ' Needles Landed On The Lines \n'
    'Our Estimation of pi is: (2 * Amount Of Needles * Length Of Needle)/(Number Of Needles On Lines * Line Spacing) \n'
    '(2 * ' + str(needamt) + ' * ' + str(needleng) + ')/(' + str(buffcount) + ' * ' + str(linespac) + ') = ' + str(float(piest))))
    titlelab.place(x=550, y= 400, anchor = 'center') #place title where necessary

sliders = {} #prep variable for sliders to be used

lbl = tk.Label(root, text="Number of Lines").pack(anchor = 'nw') #label of slider then places
sliders["Number of Lines"] = tk.Scale(root, from_ = 5, to = 50, orient='horizontal') #slider widget to decide value
sliders["Number of Lines"].pack(anchor = 'nw') #place slider widget

lbl = tk.Label(root, text="Number of Needles").pack(anchor = 'nw')
sliders["Number of Needles"] = tk.Scale(root, from_ = 5, to = 1000, orient='horizontal')
sliders["Number of Needles"].pack(anchor = 'nw')

for name in ["Length of Needles" , "Space Between Lines" , "Length of Lines"]: #loop for sliders that require same ranges of values
    lbl = tk.Label(root, text=name).pack(anchor = 'w')
    
    scl = tk.Scale(root, from_ = 5, to = 20, orient='horizontal' , resolution = 0.01)
    scl.pack(anchor = 'w')
    
    sliders[name] = scl


tk.Button(root , text = "Generate Image" , command = getchart , bg = 'red').pack(anchor = 'sw') #button placed that causes a function to run when pressed

root.mainloop()



