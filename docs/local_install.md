# Local Installation

This is a guide to get the application running locally
for development.

## Notes

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

`cp rapidpro_for_health/settings/local.py.example rapidpro_for_health/settings/local.py`

## Build the static files

ToDo: This will depend on the tools we choose to use.

## Create a database.

The default settings use postgresql and use the db name
`rapidpro_for_health` through a local connection (without username or
password)

### Run the migrations

Once the DB is available, run the project migrations:

`manage.py migrate`

## Create a super user or import a test db

To create a super user run:

`manage.py createsuperuser`

To import a db:

`psql -d rapidpro_for_health < rpfh_db_backup.sql`

## Run the local server

`manage.py runserver`

Check the site at `http://localhost:8000`

# Running the tests

`./scripts/runtests.sh`

