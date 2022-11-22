#!/usr/bin/env python3
"""
This module contains the code for rendering the starred
projects on GitHub
"""

from app import app
from flask import abort, jsonify, request, make_response
# from config import ACCESS_TOKEN
import json
from plotly.graph_objs import Bar
import requests

url = "https://api.github.com/"
header = {
    "Accept": "application/vnd.github+json",
    # "Authorization": "token {}".format(ACCESS_TOKEN),
}
sort = ">10&sort=stars&per_page=100"


@app.route("/top_starred_repos", methods=["GET"], strict_slashes=True)
def get_top_starred_repos():
    """
    This endpoint returns top starred repositories
    on GitHub irrespective of language used
    """
    # session = requests.session()
    # sort = ">10&sort=stars&per_page=100"
    search_starred_repos = '{}search/repositories?q=stars:{}'.format(url, sort)
    r = requests.get(search_starred_repos, headers=header)

    if r.status_code != 200:
        raise ValueError('Cannot retrieve data from requested endpoint')

    top_starred_repos_dict = r.json()
    top_starred_repos = top_starred_repos_dict['items']

    repo_name, repo_url, repo_owner, stars = [], [], [], []

    for starred_repos in top_starred_repos:
        repo_names = starred_repos["name"]
        repo_urls = starred_repos["html_url"]
        repo_owners = starred_repos["owner"]["login"]

        repo_name.append(repo_names)
        repo_url.append(repo_urls)
        repo_owner.append(repo_owners)
        stars.append(starred_repos["stargazers_count"])

    data = [repo_name, repo_url, repo_owner, stars]

    # return repo_name, repo_url, repo_owner
    # return top_starred_repos
    return data


@app.route("/language/<language>", methods=["GET"], strict_slashes=True)
def get_stars_by_language(language):
    """ This endpoint returns top starred projects by language """

    search_language = "{}search/repositories?q=language:{}&sort=stars".format(url, language)
    r = requests.get(search_language, headers=header)

    if r.status_code != 200:
        raise ValueError('Cannot retrieve data from requested endpoint')

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


@app.route("/owners/", methods=["GET"], strict_slashes=True)
def get_repo_owner():
    """ This endpoint return info on the owner/organization of a requested repo """
    # sort = ">1000&sort=stars&per_page=100"
    search_owner = "{}users?q=stars:{}".format(url, sort)
    r = requests.get(search_owner, headers=header)

    if r.status_code != 200:
        raise ValueError('Cannot retrieve data from requested endpoint')

    response_dict = json.loads(r.content)
    # owner_dicts = response_dict["total_count"]
    # total_users = "Total users: {}".format(owner_dicts)
    return response_dict


@app.route("/organizations", methods=["GET"], strict_slashes=True)
def get_starred_orgs():
    """ This endpoint returns top starred organizations """
    # sort = ">1000&sort=stars&per_page=100"
    get_starred_orgs = "{}search/users?q=type:org&sort:{}".format(url, sort)
    r = requests.get(get_starred_orgs)

    if r.status_code != 200:
        raise ValueError('Cannot retrieve data from requested endpoint')

    response_dict = r.json()
    repo_dicts = response_dict["items"]

    return response_dict
    # return repo_dicts
