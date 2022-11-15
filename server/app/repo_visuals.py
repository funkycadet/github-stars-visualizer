#!/usr/bin/env python3
"""
Repo Visuals
    This module creates a visual representation of the starred repositories
    per language a user would like to see using Ploty as its data visualization
    tool.
"""
from plotly.graph_objects import Bar
from plotly import offline
import requests


# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
header = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=header)
print("Status code: {}".format(r.status_code))

# Process result
response_dict = r.json()
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print("\nKeys: {}".format(len(repo_dict)))
for key in sorted(repo_dict.keys()):
    print(key)

