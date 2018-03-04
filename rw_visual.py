
#  Plot the Random Walk

# Generating multiple random walks

# Every random walk is different; to make multiple walks
#   wrap it in a while loop;import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

#from random_walk import RandomWalk

# Keep making new walks as long as te program is active

# This code will generate a random walk, display it in matplotlib's
#    viewer. When we close the viewer, we'll be asked whether we want
#    to generate another walk. Answer y and we should be able to 
#    generate walks that stay near the starting point. Enter n to end
#    the program

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    #plt.scatter(rw.x_values, rw.y_values, s=15)
    #plt.show()

    #keep_running = input("Make another walk? (y/n):")
    #if keep_running == 'n':
	    #break

#  Styling the walk

#  Coloring the points

#  Use range() to get a list of numbers equal to the number of points in the walk
#  Store them in the list point_numbers; set the color for each point
#  Pass point_numbers to the c arg and pass edgecolor=none 

#import matplotlib.pyplot as plt

#  Set size of plotting window

    plt.figure(dpi=128, figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=15)
    #plt.show()

    #keep_running = input("make another walk?) (y/n): ")
    #if keep_runing =='n':
        #break

#  Plotting the starting and ending points

    plt.scatter(0, 0, c='green', edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],c='red', edgecolor='none', s=100)

    #plt.show()

#keep_running = input("Make another walk? (y/n): ")
#if keep_running == 'n':
#   break

#  Remove the Axes

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show() 

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break 



       




                















