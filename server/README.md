# Server

This directory contains files and folders for the server section of the project.

## Server Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

## General workflow

By default, the dependencies are managed with [Poetry](https://python-poetry.org/). Make sure to visit the URL and install Poetry if you don't have it on your system.

To start a shell session with Poetry, run:

```console
$ poetry shell
```

in the server directory: `/server`.

From `/server`, you can install all the dependencies with:

```console
$ poetry install
```

This should be done after activating the shell.

Next, open your editor at the project root, `./github-stars-visualizer`, so that you can see the `./server`, `./tests` and other project directories and files. That way, your editor would be able to locate all imports. Make sure your editor uses the environment you just created with Poetry.

To run the backend, run
```console
./server/main.py
```

in the root of the project on your terminal so as to test the endpoints available.

## Code contributions

While making contributions to the code, make sure you're working on the `updates` branch as pushes to the `main` branch are not allowed to avoid merge conflicts on the `main` branch.

## Endpoints

The following are the endpoints for the server-side of the project:

* /api/v1/top_starred_repos
* /api/v1/language/<language>
* /api/v1/owner/  [in view]
* /api/v1/organizations  [in view]