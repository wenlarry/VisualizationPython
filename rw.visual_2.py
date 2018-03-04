# re.visual_2.py

#  Adding plot points

# Creates a random walk with 50000 points and plots each point at size =1.
# The resulting walk is wispy and cloud-like

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

