#  Add a line after the loop to return NONE if the cty name
#    is not found

from pygal.maps.world import COUNTRIES 

def get_country_code(country_name):
    """Return the Pygal 2 digit country code for the given country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

#print(get_country_code('Andorra'))
#print(get_country_code("United Arab Emirates"))
