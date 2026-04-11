# Claude Skills Marketplace

This project utilises Mkdocs with the Material theme and Mermaid for
diagrams. Currently the docs are published using github actions on github pages
from the branch gh-pages, which contains static site files generated from
Markdown documents and assets. The overall configuration of the site is
stored in mkdocs.yml in the root directory of the repo. If making contributions
to docs, it can be useful to host it locally to see the effect of changes.

## Project layout (root directory)

    mkdocs.yml                # The configuration file
    requirements.txt          # mkdocs requirements file for pip, used to locally install mkdocs and its plugins (normally in a Python venv)
    dockerfile                # Docker manifest for locally serving the site through a container (alternative to locally installing mkdocs)
    docs/                     # Documentation files in Markdown (.md), subfolders for /img, /assets, /stylesheets, /css, etc.

## Setting up and serving MkDocs locally (Linux)

A `Makefile` in the repo root handles setup and serving for you. You don't need to manually create a venv, activate it, or install requirements.

1. Clone repo and cd to its root:

    ```bash
    git clone git@github.com:jjainschigg-r/claude-skills-marketplace.git
    cd claude-skills-marketplace
    ```

2. See available make targets:

    ```bash
    make help
    ```

3. Serve the site to 127.0.0.1:8000 (auto-runs setup if needed, live-reloads on file changes):

    ```bash
    make serve
    ```

    That's it. `make serve` will create the venv and install all dependencies from `requirements.txt` automatically if they aren't already present.

4. Create a feature branch for your changes:

    ```bash
    git checkout main
    git pull origin main
    git checkout -b my-feature-branch
    (make changes)
    git push -u origin my-feature-branch  # push to origin and file Pull Request
    ```

5. To clean up the local venv:

    ```bash
    make clean
    ```

## Use containerized mkdocs instead (assumes you have Docker installed locally)

1. Build the container from the provided Dockerfile

    ```bash
    docker build -f Dockerfile -t mk-local
    ```

2. Clone repo as in Step 1, above, and cd to repo root

3. Create and checkout your working branch, as in steps 4 and 5, above.

4. Open a new terminal session (so you can stop the container later by pressing CTRL-C) and run the container

    ```bash
    docker run --rm -it -p 8000:8000 -v ${PWD}:/docs mk-local
    ```

# Documentation Standards

By default, we follow the [Kubernetes documentation style guide](https://kubernetes.io/docs/contribute/style/style-guide/). 

## Header Capitalization

All header text should be capitalized.

