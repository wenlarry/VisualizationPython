#  Rolling Dice of different sizes

#  The largest result is now 16

from die import Die

import pygal

#  Create a D6 and a D10
die_1 = Die()
# die_2 = Die(10)
die_2 = Die () 

# Rolls and store results
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze results
frequencies =[]
#max_result = die_1.num_sides + die_2.num_sides
max_result = 6 + 10 

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize result
hist = pygal.Bar()

hist.title = "Results - Rolling a D6 and D10 - 50000 times"
hist.x_labels =['2','3','4','5','6','7','8','9','10','11','12',
                '13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10' ,frequencies)
hist.render_to_file('dice_visual_size.svg')
