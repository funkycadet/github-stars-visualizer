#!/usr/bin/env python3
"""
This module contains the code for rendering the starred
projects on GitHub
"""

from app import app
from flask import abort, jsonify, request, make_response
# from config import ACCESS_TOKEN
from plotly.graph_objs import Bar
import requests

url = "https://api.github.com/search/"
header = {
    "Accept": "application/vnd.github+json",
    # "Authorization": "token {}".format(ACCESS_TOKEN),
}


@app.route("/top_starred_repos", methods=["GET"], strict_slashes=True)
def get_top_starred_repos():
    """
    This endpoint returns top starred repositories
    on GitHub irrespective of language used
    """
    session = requests.session()
    sort = ">0&sort=stars&per_page=100"
    search_top_starred_repos = '{}repositories?q=stars:{}'.format(url, sort)
    r = requests.get(search_top_starred_repos, headers=header)

    if r.status_code != 200:
        raise ValueError('Cannot retrieve from {}'.format())

    top_starred_repos_dict = r.json()
    top_starred_repos = top_starred_repos_dict['items']
    return top_starred_repos


@app.route("/language/<language>", methods=["GET"], strict_slashes=True)
def get_stars_by_language(language):
    """ This endpoint returns top starred projects by language """

    search_language = "{}repositories?q=language:{}&sort=stars".format(url, language)
    r = requests.get(search_language, headers=header)

    if r.status_code != 200:
        raise ValueError('Cannot retrieve from {}'.format())

    response_dict = r.json()
    repo_dicts = response_dict["items"]

    repo_links, stars, labels = [], [], []

    for repo_dict in repo_dicts:
        repo_name = repo_dict["name"]
        repo_url = repo_dict["html_url"]
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict["stargazers_count"])

        owner = repo_dict["owner"]["login"]
        description = repo_dict["description"]
        label = f"{owner}<br />{description}"
        labels.append(label)

    # Make visualization
    data = [
        {
            "type": "bar",
            "x": repo_links,
            "y": stars,
            "hovertext": labels,
            "marker": {
                "color": "rgb(60, 100, 150)",
                "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
            },
            "opacity": 0.6,
        }
    ]

    data_layout = {
        "title": "GitHub Stars Visualizer",
        "titlefont": {"size": 28},
        "xaxis": {
            "title": "Repository",
            "titlefont": {"size": 24},
            "tickfont": {"size": 14},
        },
        "yaxis": {
            "title": "Stars",
            "titlefont": {"size": 24},
            "tickfont": {"size": 14},
        },
    }

    figure = {"data": data, "layout": data_layout}
    return figure


@app.route("/owner/<owner>", methods=["GET"], strict_slashes=True)
def get_repo_owner(owner):
    """ This endpoint return info on the owner/organization of a requested repo """
    search_owner = "{}repositories?q=stars:{}".format(url)
