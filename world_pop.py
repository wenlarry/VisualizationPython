#  Mapping global Data Sets: JSON Format

#  Download the file 'population_data.json' from 
#    http://data.okfn.org
#  Import json to load the data properly and store
#    the data in pop_data
#  The json.load() function converts the data into
#    a format that Python can work with.
#   Loop through each item in pop_data. Each item is
#    a dict with four key value pairs; store each dict
#    in pop_dict
#  Look for 2010 in the 'Year' key of each dict.(As the
#    values in in population_data.json are all in quotes,
#     do a string comparison)
#  If the year is 2010, store the value associated with 'Country Name'
#    in country_name and the value associated with 'Value' in 
#    population

#  Converting Strings into numerical values
#    Every key and value in population_data.json is stored as a
#    string. to work with the pop data, we convert the pop strings
#    to numerical values using the int() function. Now each pop value
#    is in numerical format so when we print the pop value, we convert
#    it to a string i.e. str(population)
#
#    Often raw data is not formatted consistently, so we have errors.
#    If the error relates to decimals, we convert the string to a float
#    and then convert that float to an integer
#
#  Obtaining 2 digit Country Code
#    Before using the function in cty_code.oy, remove the print statements
#    After extracting the country name and pop, we store the cty code in
#    code or NONE. If a code is returned, the code and cty; pop are printed
#    If the code is not available, an Error msg with the cty name is displayed
#    
#  Plotting a complete Pop Map
#   
#    Create an empty dict to store cty codes and pop in Pygal formats.
#    Build the cc-population dict using the cty code as key and the pop as
#      value
#    Remove all print statements
#    add() - pass it the dict of cty codes and pop values
#
#  Grouping countries by Pop
# 
#    Create an empty dict for each cat. Loop thru cc_populations to check
#      the pop of each cty
#    The if-elif-else block adds an entry to the appropriate dict for each
#      cty code - pop pair
#    Print the length of each dict to find put the size of the groups
#
#  Styling World Maps in Pygal
#
#    See attached description of the chosen styles

import json

from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from cty_codes import get_country_code

filename='population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        #population = pop_dict['Value']
        #population = int(pop_dict['Value'])
        population = int(float(pop_dict['Value']))
        #print(country_name + ": " + population)
        #print(country + ": " + str(population))
        #code = get_country_code(country_name)
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

cc_pops_1, cc_pops_2, cc_pops_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop 

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)  
wm.title = 'World Pop in 2010, by Country'
#wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('.1bn', cc_pops_3)

wm.render_to_file('world_pop.svg')
  
            #print(code + ": " + str(population))
        #else:
            #print('ERROR - ' + country_name)
