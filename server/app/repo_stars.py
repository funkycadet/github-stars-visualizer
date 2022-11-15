#!/usr/bin/env python3
import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
header = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=header)
print("Status code: {}".format(r.status_code))

# Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print("\nKeys: {}".format(len(repo_dict)))
for key in sorted(repo_dict.keys()):
    print(key)

# Process result
print(response_dict.keys())
