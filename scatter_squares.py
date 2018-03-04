scatter_squares.py

#  Printing & Styling Individual Points with scatter()

#  Plotting a series of points with scatter()

import matplotlib.pyplot as plt

plt.scatter(2,4, s=200)

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values, y_values, s=100) 

#  set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#   set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

#  Calculating Data automatically
import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

#  set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#   set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show() 

#  Removing outlines from data points

#  plt.scatter(x_values, y_values, edgecolor='none', s=40)

#  Defining Custom Colors

#  plt.scatter(x_values, y_values, c='red', edgecolor ='none', s=40) 

#  Define colors using RGB; pass the c arg a tuple with three decimals
#     using values btw 0 and 1. Values closer to 0 produce dark colors

#  plt.scatter(x_values, y_values, c=(0,0,0.8), edgecolor='none', s=40)

#  Using a Colormap

#  A colormap is a series of colors in a gradient that moves from starting 
#     to ending color. The pyplot module includes a set of built-in colormaps

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolor='none',s=40)

#  set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.show()

#  See all the colormaps available in pyplot at http:/matplotlib.org/. Goto 
#     Examples, scroll down to Color Examples and click colormaps_reference

#  Saving plots automatically

#  Replace the call to plt.show() with a call to plt.savefig():

#  The second arg in the following code trims extra whitespace around the plot

#  plt.savefig('squares_plot.png', bbox_inches=tight)
    








