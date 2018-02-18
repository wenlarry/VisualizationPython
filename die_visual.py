
#  Rolling the Die

from die import Die

#   Create a D6
die = Die()

#  Make some rolls, and store results in a list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

#print(results)

#  Analyzing the results

#  We can increase the number of simulated rolls to 1000 
#  We create empty list frequencies to store the number of
#      times each value is rolled
#  We loop thru the possible values (1 thru 6 in this case)
#  Count how many times each number appears and append the value
#  to the frequencies list.
frequencies = []
# for value in range(1, die.num_sides+1):
for value in range(1, 6 + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

# print(frequencies)

#  A Histogram

#  Render the chart to a SVG file (.svg extension). Open the tab in 
#      any web browser and then open the file die_visual_svg. We can use
#      google
import pygal

from die import Die

#   Create a D6
die = Die()

#  Make some rolls, and store results in a list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

frequencies = []
# for value in range(1, die.num_sides+1):
for value in range(1, 6 + 1):
	frequency = results.count(value)
	frequencies.append(frequency)   

hist = pygal.Bar()

hist.title = "Results: Rolling one D6 100 times"
hist.x_labels =['1','2','3','4','5','6']
hist.x_title = "result"
hist.y_title = "frequency results"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
