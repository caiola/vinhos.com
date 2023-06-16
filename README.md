# Vinhos.com [![CircleCI](https://circleci.com/gh/antkahn/flask-api-starter-kit/tree/master.svg?style=svg)](https://circleci.com/gh/antkahn/flask-api-starter-kit/tree/master) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/antkahn/flask-api-starter-kit/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/antkahn/flask-api-starter-kit/?branch=master)

Welcome to Vinhos.com, the revolutionary open source platform for all things and wines!
Our mission is to bring the wine industry into the 21st century by sharing knowledge and source code openly.

With Vinhos.com, winemakers and wine enthusiasts alike can access a wealth of information and resources to help them create the perfect vintage.

Whether you're a seasoned pro looking to improve your craft or a budding enthusiast looking to learn more about the art of winemaking, Vinhos.com has something for everyone.

So join us on this journey of discovery and let's make a revolution together!

## NOTE: Work in progress, documentation changes and instability is expected

The primary goal of this project is to have a website working with API documented.

## Sponsors
[![Alt text](/docs/images/logo_moqups.png)](https://moqups.com/)
Sponsored a free subscription for one year.


## Installation Guide
[Installation Guide](./setup/installation.md)


## Architecture

<svg width="600" height="300">
  <rect x="20" y="20" width="120" height="120" rx="10" fill="#efefef" />
  <rect x="180" y="20" width="120" height="120" rx="10" fill="#efefef" />
  <rect x="340" y="20" width="120" height="120" rx="10" fill="#efefef" />
  <rect x="20" y="160" width="120" height="120" rx="10" fill="#efefef" />
  <rect x="180" y="160" width="120" height="120" rx="10" fill="#efefef" />
  <text x="50" y="90" font-size="14" fill="#333333">Monitoring</text>
  <text x="210" y="90" font-size="14" fill="#333333">Backoffice</text>
  <text x="50" y="230" font-size="14" fill="#333333">Frontend</text>
  <text x="210" y="230" font-size="14" fill="#333333">API</text>
  <text x="370" y="90" font-size="14" fill="#333333">Database</text>
</svg>


## Table of Contents

1. [Dependencies](#dependencies)
1. [Getting Started](#getting-started)
1. [Commands](#commands)
1. [Database](#database)
1. [Application Structure](#application-structure)
1. [Development](#development)
1. [Testing](#testing)
1. [Lint](#lint)
1. [Format](#format)
1. [Swagger](#swagger)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone https://github.com/caiola/vinhos.com.git <my-project-name>
$ cd <my-project-name>
```

## Local Development
In order to run a local development environment:
1. Copy `.env.sample` to a `.env` file and change values if needed
2. `docker-compose up -d`
3. `docker-compose exec app bash`
4. To start a development server `flask run --host 0.0.0.0`

## Local Deployment

```bash
$ make server.install      # Install the pip dependencies on the docker container
$ make server.start        # Run the container containing your local python server
```

If everything works, you should see the available routes [here](http://127.0.0.1:3000/application/spec).

The API runs locally on docker containers. You can easily change the python version you are willing to use [here](https://github.com/antkahn/flask-api-starter-kit/blob/master/docker-compose.yml#L4), by fetching a docker image of the python version you want.

## Commands

You can display availables make commands using `make`.

While developing, you will probably rely mostly on `make server.start`; however, there are additional scripts at your disposal:

| `make <script>`      | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| `help`               | Display availables make commands                                             |
| `server.install`     | Install the pip dependencies on the server's container.                      |
| `server.start`       | Run your local server in its own docker container.                           |
| `server.daemon`      | Run your local server in its own docker container as a daemon.               |
| `server.upgrade`     | Upgrade pip packages interactively.                                          |
| `database.connect`   | Connect to your docker database.                                             |
| `database.migrate`   | Generate a database migration file using alembic, based on your model files. |
| `database.upgrade`   | Run the migrations until your database is up to date.                        |
| `database.downgrade` | Downgrade your database by one migration.                                    |
| `test`               | Run unit tests with pytest in its own container.                             |
| `test.coverage`      | Run test coverage using pytest-cov.                                          |
| `test.lint`          | Run flake8 on the `src` and `test` directories.                              |
| `test.safety`        | Run safety to check if your vendors have security issues.                    |
| `format.black`       | Format python files using Black.                                             |
| `format.isort`       | Order python imports using isort.                                            |

## Database

The database is in [PostgreSql](https://www.postgresql.org/).

Locally, you can connect to your database using :

```bash
$ make database.connect
```

However, you will need before using this command to change the docker database container's name [here](https://github.com/antkahn/flask-api-starter-kit/blob/master/package.json#L6).

This kit contains a built in database versioning using [alembic](https://pypi.python.org/pypi/alembic).
Once you've changed your models, which should reflect your database's state, you can generate the migration, then upgrade or downgrade your database as you want. See [Commands](#commands) for more information.

The migration will be generated by the container, it may possible that you can only edit it via `sudo` or by running `chown` on the generated file.

## Application Structure

The application structure presented in this boilerplate is grouped primarily by file type. Please note, however, that this structure is only meant to serve as a guide, it is by no means prescriptive.

```
.
├── devops                   # Project devops configuration settings
│   └── deploy               # Environment-specific configuration files for shipit
├── migrations               # Database's migrations settings
│   └── versions             # Database's migrations versions generated by alembic
├── src                      # Application source code
│   ├── models               # Python classes modeling the database
│   │   ├── abc.py           # Abstract base class model
│   │   └── user.py          # Definition of the user model
│   ├── repositories         # Python classes allowing you to interact with your models
│   │   └── user.py          # Methods to easily handle user models
│   ├── resources            # Python classes containing the HTTP verbs of your routes
│   │   └── user.py          # Rest verbs related to the user routes
│   ├── routes               # Routes definitions and links to their associated resources
│   │   ├── __init__.py      # Contains every blueprint of your API
│   │   └── user.py          # The blueprint related to the user
│   ├── swagger              # Resources documentation
│   │   └── user             # Documentation of the user resource
│   │       └── GET.yml      # Documentation of the GET method on the user resource
│   ├── util                 # Some helpfull, non-business Python functions for your project
│   │   └── parse_params.py  # Wrapper for the resources to easily handle parameters
│   ├── config.py            # Project configuration settings
│   ├── manage.py            # Project commands
│   └── server.py            # Server configuration
└── test                     # Unit tests source code
```

## Development

To develop locally, here are your two options:

```bash
$ make server.start           # Create the containers containing your python server in your terminal
$ make server.daemon          # Create the containers containing your python server as a daemon
```

The containers will reload by themselves as your source code is changed.
You can check the logs in the `./server.log` file.

## Testing

To add a unit test, simply create a `test_*.py` file anywhere in `./test/`, prefix your test classes with `Test` and your testing methods with `test_`. Unittest will run them automaticaly.
You can add objects in your database that will only be used in your tests, see example.
You can run your tests in their own container with the command:

```bash
$ make test
```

## Lint

To lint your code using flake8, just run in your terminal:

```bash
$ make test.lint
```

It will run the flake8 commands on your project in your server container, and display any lint error you may have in your code.

## Format

The code is formatted using [Black](https://github.com/python/black) and [Isort](https://pypi.org/project/isort/). You have the following commands to your disposal:

```bash
$ make format.black # Apply Black on every file
$ make format.isort # Apply Isort on every file

# Some tests with flake8
# docker run --rm -v $(pwd):/app alpine/flake8:latest sh -c "flake8 -v --color always --show-source --statistics --benchmark"
```

## Swagger

Your API needs a description of it's routes and how to interact with them.
You can easily do that with the swagger package included in the starter kit.
Simply add a docstring to the resources of your API like in the `user` example.
The API description will be available [here](http://127.0.0.1:3000/application/spec).
The Swagger UI will be available [here](http://127.0.0.1:3000/apidocs/).

## Running locally on Windows

```
pip install poetry
poetry install
```

## To add networking and misc tools use docker image "image: busybox"

```
  tools:
    image: busybox
```

## Database migrations

Enter apiserver
```
# docker-compose -f docker-compose-local.yml exec apiserver sh
make local.apiserver.go
```

Update migrations

```
flask db upgrade
```

Run seeds

```
flask seed_db
```

Add a new database migration
```
flask db migrate -m "Schema"
flask db migrate -m "Add unique constraint to Ad model"
flask db migrate -m "Add account changes"
flask db migrate -m "Add store field account_id"
flask db migrate -m "Add table grape variety"
flask db migrate -m "Change grape variety field name"
```


Poetry 
```
# Deprecated dependencies retturn this issue
# poetry 'HTTPResponse' object has no attribute 'strict'
# Need to do a reinstallation on the container

make local.force

# if container is running
docker-compose -f docker-compose-local.yml exec apiserver sh -c "poetry lock"

# container not running
# linux
# docker run -it --rm -v $(pwd):/app -w /app python:3.10 /bin/bash -c "pip install poetry && poetry lock"
# windows
# docker run -it --rm -v %cd%:/app -w /app python:3.10 /bin/bash -c "pip install poetry && poetry lock"

# windows
cd backend
docker build -t img-local-poetry -f backend/dockerfile-apiserver-local ./backend
docker run -it --rm -v %cd%:/app -w /app img-local-poetry /bin/bash -c "poetry lock"

# Run tests with poetry
poetry add --group dev factory-boy
poetry  --extras dev run pytest
```
## Black

Run code formatter
```
# Verify changes
poetry run black . --check
poetry run isort . --profile black --check

# Apply changes
poetry run black .
poetry run isort . --profile black

```

