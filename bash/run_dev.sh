#!/usr/bin/bash

# activating the python virtual environment
source venv/bin/activate

# setting up the FLASK environemnt variables
export FLASK_APP=app.py         # setting the flask app
export FLASK_ENV=development    # setting the environment to development
export FLASK_DEBUG=1            # setting the debug flag to true

# making sure that the database is up to date with the most recent changes
# this should keep the current data in the database while only updating the
# structure of the database
alembic revision --autogenerate
alembic upgrade head

# running the application
flask run
