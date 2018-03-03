# Building a World Map

# americas.py

from pygal.maps.world import World 

wm = World()
wm.title = 'North, Central, and South America'

wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','pa','sv'])
wm.add('South America',['ar','br','co','gy','py','sr','uy','ve'])

wm.render_to_file('americas.svg')

