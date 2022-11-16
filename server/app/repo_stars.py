#!/usr/bin/env python3
"""
This module contains the code for rendering the starred
projects on GitHub
"""

from app import app
from flask import abort, jsonify, request, make_response
from plotly.graph_objs import Bar
import requests
import sys


@app.route("/language/<language>", methods=["GET"], strict_slashes=True)
def get_stars_by_language(language):
    """ This method returns top starred projects by language """

    url = 'https://api.github.com/search/repositories?q=language:{}&sort=stars'.format(language)
    header = {'Accept': 'application/vnd.github+json'}

    r = requests.get(url, headers=header)

    response_dict = r.json()
    repo_dicts = response_dict['items']
    # repo_dict = repo_dicts[0]

    repo_links, stars, labels = [], [], []

    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    # for key in sorted(repo_dict.keys()):
    #     keys = key

    # Make visualization
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    data_layout = {
        'title': 'GitHub Stars Visualizer',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }

    # Process result
    # keys = response_dict.keys()
    # result = [
    #     "Status code: {}".format(r.status_code),
    #     f"Total repositories: {response_dict['total_count']}",
    #     f"Repositories returned: {len(repo_dicts)}",
    #     f"Keys: {len(repo_dict)}",
    #     f"{keys}"
    # ]
    # return(result)

    figure = {'data': data, 'layout': data_layout}
    return figure
