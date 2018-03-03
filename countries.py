#  Obtaining 2 digit Country Codes

#  Before mapping - countries need to be in country code and 
#    pop as values. Required by Pygal mapping tool
#  Pygal's dict COUNTRIES contain the two-letter country codes
#    as keys and the country names as values. 
from pygal.maps.world import COUNTRIES 

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code]) 
