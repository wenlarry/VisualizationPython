# mpl_squares.py

#  Plotting a Simple line graph

#  Changing label type and graph thickness 

#  Correcting the plot

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares, linewidth=5)

# set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
