# GitHub Stars Visualizer

A web service that allows you to visualize top starred projects on Github.

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

### General workflow

By default, the dependencies are managed with [Poetry](https://python-poetry.org/). Make sure to visit the URL and install Poetry if you don't have it on your system.

To start a shell session with Poetry, run:

```console
$ poetry shell
```

in the project root: `./github-stars-visualizer`.

From the project root, you can install all the dependencies with:

```console
$ poetry install
```

This should be done after activating the shell.

Next, open ypur editor at the project root so that you can see an `./app` directory alongside the `./tests` directory with the project code alongside other project files. That way, your editor would be able to locate all imports etc. Make sure your editor uses the environment you just created with Poetry.

