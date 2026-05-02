import numpy as np #import necessary packages
import matplotlib.pyplot as plt
import math
from math import sin, cos, tan
import random
rng = np.random.default_rng() #for generating throwing of needles

print('This porgram is designed to estimate pi using Buffons Needle Problem')
lineamt = int(input('How Many Lines Would You Like to Use?')) #set number of lines to positive integer chosen value
while lineamt <= 0:
    lineamt = int(input('How Many Lines Would You Like to Use? Pick Integer Value More Than 0'))
needamt = int(input('How Many Needles Would You Like to Use?')) #set number of needles to positive integer chosen value
while needamt <= 0:
    needamt = int(input('How Many Needles Would You Like to Use? Pick Integer Value More Than 0'))
needleng = float(input('What Length of Needles Would You Like to Use?')) #set length of needle to positive chosen value
while needleng <= 0:
    needleng = float(input('What Length of Needles Would You Like to Use? Pick Value More Than 0'))
linespac = float(input('What Spacing Between Lines Would You Like to Use?')) #set spacing of lines to positive chosen value
while linespac <= 0:
    linespac = float(input('What Spacing Between Lines Would You Like to Use? Pick Value More Than 0'))
linelen = float(input('What Length Lines Would You Like to Use?')) #set length of lines to positive chosen value
while linelen <= 0:
    linelen = float(input('What Length Lines Would You Like to Use? Pick Value More Than 0'))

linefirst = linespac / 2 #set variable for line positioning of first line
linelast =  (linespac / 2) + ((lineamt - 1)*linespac) #set variable for line positioning of last line
linesetup = np.linspace(linefirst, linelast, lineamt) #set up lines to be thrown on to
xlimit = linelast + (linespac / 2) #set axis limits for needles
ylimit = linelen 

randstarx = rng.uniform(low = 0, high = xlimit, size = needamt) #give random start positions of needles x
randstary = rng.uniform(low = 0, high = ylimit, size = needamt) #and y
randang = rng.uniform(low = 0 , high = 2 * math.pi  , size = needamt) #give random angles of needles

randendx = np.empty(needamt) #set up empty arrays to fill with end points of the needles
randendy = np.empty(needamt)
fig, ax = plt.subplots() #prepare plotting
ax.vlines(linesetup, 0 , ylimit , linestyles = 'dotted' , colors = 'r') #plot vertical lines on plot
for endcalc in range(needamt): #for all needles
    randendx[endcalc] = randstarx[endcalc] + (needleng * cos(randang[endcalc])) #calculate end x and y point of the needles given the start points and angles
    randendy[endcalc] = randstary[endcalc] + (needleng * sin(randang[endcalc]))

    ax.plot([randstarx[endcalc],randendx[endcalc]],[randstary[endcalc],randendy[endcalc]]) #plot each needle as line on chart
    ax.set_xlim(0,xlimit) #set range for axes
    ax.set_ylim(0,ylimit)

buffcount = 0 #initialise counter for needles on lines
for hitline in linesetup: #for each line
    for buffcheck in range(needamt): #for each needle
        if randstarx[buffcheck] <= hitline <= randendx[buffcheck] or randstarx[buffcheck] >= hitline >= randendx[buffcheck]: #check if needle coords go over a line
            buffcount += 1 #add to counter if they do

piest = ((2 * needamt) * needleng) / (buffcount * linespac) #calculate the pi estimation based on the number of needles thrown and the number of needles that land on a line

ax.set_title(str(lineamt) + ' Lines, ' + str(needamt) + ' Needles, ' + str(needleng) + ' Needle Length and ' + str(linespac) + ' Line Space \n' + #preparing title
str(buffcount) + ' Needles Landed On The Lines \n'
'Our Estimation of pi is: (2 * Amount Of Needles * Length Of Needle)/(Number Of Needles On Lines * Line Spacing) \n'
'(2 * ' + str(needamt) + ' * ' + str(needleng) + ')/(' + str(buffcount) + ' * ' + str(linespac) + ') = ' + str(float(piest)))
ax.set_aspect('equal', adjustable='box')

plt.show() #show chart


