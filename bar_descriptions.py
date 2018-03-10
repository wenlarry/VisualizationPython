# bar_description.py

#  Adding custom tooltips

#  Hovering the cursor over an individual bas shows the info the bar represents
#   called a tooltip
#  Pass a list of dict to add() instead of a list of values.

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
