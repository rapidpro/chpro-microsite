# Local Installation

## Notes

This guide is for installing the application for local development.

To deploy the application for production, follow ...(ToDo)

### Make sure you have the correct python version

The application was developed using Python 3.6.1.
To make sure everything works as expected, make sure you have
the correct version of python.

### Make sure you're in the correct directory

All commands in this guide are assumed to be run from the project root.

## Install the app

### Install pipenv

If you don't already have it, install `pipenv`:

```
pip install -U pipenv
```

### Install the project

Install the development dependencies:

```
pipenv install -d
```

Use `pipenv shell` to "activate" your Python virtual environment
when working on the project.

### Copy the local settings and modify as needed

`cp rh/settings/local.py.example rh/settings/local.py`

## Build the static files

### Requirements

This step requires you have installed NodeJS and yarn.
Any new version should work, but the code has been tested with:

 * Node: 9.4.0
 * NPM: 5.6.0
 * yarn: 1.4.0

## Compiling

Install the dependencies from the project's root:

`yarn`

This will install the dependencies and compile the staticfiles.

To manually compile afterwards use:

`yarn build`

or:

`yarn watch`

This will watch the files in the client directory and recompile them if
there are changes. The entrypoint is `rh/client/all.js`.

## Create a database.

The default settings use postgresql and use the db name
`rh` through a local connection (without username or
password)

### Run the migrations

Once the DB is available, run the project migrations:

`manage.py migrate`

## Create a super user or import a test db

To create a super user run:

`manage.py createsuperuser`

To import a db:

`psql -d rh < rpfh_db_backup.sql`

## Run the local server

`manage.py runserver`

Check the site at `http://localhost:8000`

# Running the tests

`./scripts/runtests.sh`

# Generate the [Styleguide](http://localhost:8000/static/styleguide/index.html)

* Run `yarn build_guide` from `/chpro-microsite/rh/client/`
* Visit at http://localhost:8000/static/styleguide/index.html
