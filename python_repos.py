# python_repos.py

#  Processing API response

#  Make an API call and store the response
#  Use requests to make the call
#  get() and pass it the URL and store the  response in in the variable r
#  The resp0nse object has an attribute 'status_code' that tells whether the
#    request was successful.(status code of 200 indicates success)
#  store the resulting dict in response_dict

import requests

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 


url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(url)
print("Status code:", r.status_code)
response_dict = r.json()

#print(response_dict.keys())

#  Working with Response Dict

#  Total # of Python repos on Github associated with 'total_count'
#  Value associated with 'items' is a list of containing a number of dict, each
#    of which contains data about an individual Python repo. Store this list in
#    repo_dicts
#  Pull out the first item from repo dicts and store it in repo_dict. Print the
#    # of keys in the dict to see how much info. 
#  Info: 72 keys in repo_dict

print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
#print("Total Repositories", len(repo_dicts))
#print ("Repos returned:", len(repo_dicts))
#repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
	#print(key)

#  Pull out the values for some of the keys in repo_dict

#  Repo Description  - Status Code: 200; We 1)most starred project, 2)owner,
#    3)starred by # og GITHUB users, 4)URL for the project's repo, its creation
#    date and recent update, 5) description

#  Summarizing Top Repos

#  Loop thru all the dicts in repo_dicts. Inside the loop, print the name of
#    each project, owner, etc.
#  Status code: 200 . Some interesting projects in the results

#print("\nselected info about first repo:")
#print("\nselected info about each repo:")

names, stars = [], []
#names , plot_dicts = [], [] 
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#plot_dict = {
    #'value': repo_dict['stargazers_count'],
    #'label': repo_dict['description'],
    #}
    #'xlink': repo_dict['html_url'],
   # }

    #print('Name:', repo_dict['name'])
    #print('Owner:', repo_dict['owner']['login'])
    #print('Stars:', repo_dict['stargazers_count'])
    #print('Repository:', repo_dict['html_url'])
    #print('Created:', repo_dict['created_at'])
    #print('Updated:', repo_dict['updated_at'])
    #print('Description:', repo_dict['description'])
       
#plot_dicts.append(plot_dict)

#  Monitoring API Rate Limits

# How many requests can be made in a certain amount of time. To see Git Hub's limits
#   enter https://api.github.com/rate_limit into WEB BROWSER
#  If limit is reached, just wait until quota resets.

#  Visualizing Repos using Pygal

#  Import pygal and pygal styles needed for the chart
#  Print the status of the API call response and the total # of repos
#  Create 2 empty lists to store the data for the chart
#  Need the name of each project and in order to label the bars
#  In the loop, append the name of each project and # of stars
#  Define the style; Pass the base style arg to use LS
#  Use Bar() to make bar chart and pass it my_style
#  Pass 2 more style args; labels rotation and hide the legend  because plotting
#    only one series on the chart
#  Don't need the data series to be labeled; pass an empty string for the label
#    when we add the data
#  Chart - the first few projects are significantly more popular

my_style = LS('#333366', base_style=LCS)
#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
#chart.title = 'Most starred Python projects on GitHub'
#chart.x_labels = names

#chart.add('', stars)
#chart.render_to_file('python_repos.svg')

#  Refining Pygal charts

#  Modifying the attributes of my_config customize the appearance of the chart
#  Set the 2 attributes x_label_rotation and show_legend, originally passed as 
#    keyword args when we make an instance of Bar
#  Major labels are just the labels on the y-axis that mark off increments of 
#    5000 stars
#  truncate_labels to shorten the longer project names (full names pop up when we hover)
#  Hide the horizontal lines on the graph by show_y_guides to False
#  Set a custom width so the chart will use more of the available space
#  Make an instance of Bar; pass my_config as the first arg and send all our config
#    settings in one arg

my_config = pygal.Config()
my_config.x_label_rotation =46
my_config.show_legend = False
my_config.title_font_size = 23
my_config.label_font_size =12
my_config.major_label_font_size = 18
my_config.truncate_label = 16
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
#chart = pygal.Bar(style=my_style, x_label_rotation=43, show_legend=False)
chart.title = 'Most starred Python projects on GitHub'
chart.x_labels = names

chart.add('', stars)
#chart.add('', plot_dicts)
chart.render_to_file('python_repos2.svg') 

# Plotting the data

#  Make an empty list for plot_dicts
#  Inside the loop, create the dict plot_dict for each project
#  Store the number of stars with key 'value' and the project description with the key
#  'label' in each plot_dict. Append each project's plot_dict to plot_dicts. 

#  Adding clickable links to graphs

#  Allow each bar in the chart as a link to a website. Add a new key-value pair to
#    each project's plot_dict using the key 'xlink'


