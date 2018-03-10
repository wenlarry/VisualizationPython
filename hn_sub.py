#  Hacker News API

#  Make an API call and print the status of the response
#  Convert the response to a Python list that is stored in
#    submission_ids.
#  Use these IDs to build dictionaries.
#  Setup empty list 'submissions_dicts' to store these dictionaries
#  Loop thru the IDs of the top 28 submissions
#  Make an API call for each submission by generating a URL that 
#    includes the current value of submission_id. Print the status of
#    each request
#  Create a dict for the submission currently being processed where we
#    store the title of the submission and z link to the discussion page
#  Store # of comments in the dict; if the article has no comments yet, 
#    the key 'descendants' will not be present
#  'dict_get' returns the value associated with the given key if it exists
#     or the value provided if the key doesn't exist (0 in this case)
#  Append each submission_dict to the list submission_dicts

#  Sort the list of dicts by # of comments; use the function itemgetter()
#  Pass this function the key 'comments' and it pulls the value associated
#    with that key from each dict in the list.
#  The sorted() function uses this value as its basis for sorting the list
#  Once the list is sorted, loop thru the list and print 3 pieces of info
#    about each of the top submission
import requests

from operator import itemgetter

# Make an API call and store
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process info about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:28]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])



