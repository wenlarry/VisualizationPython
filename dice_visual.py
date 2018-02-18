#  Rolling Two Dice

#  Calculate the sum of 2 dice or each roll; the largest possible
#     result(12), that we store in max_result
#  When we analyze the results, we count the number of results for
#     each value btw 2 and max_result
#  This code  simulate rolling a pair of dice with any number of 
#     sides

import pygal

from die import Die

#  Create two D6 dice
die_1 = Die()
die_2 = Die()

#  Rolls and store in a list
results =[]
for roll_num in range(1000):
    #result = die_1.roll() + die_2.roll()
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze results
frequencies = []
#max_result = die_1.num_sides + die_2.num_sides
max_result = 6 + 6

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results
hist = pygal.Bar()

hist.title = "Results - Roll of two D6 dice 1000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')

