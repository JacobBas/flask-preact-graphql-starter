#!/usr/bin/bash

# activating the python virtual environment
source venv/bin/activate

# running the application
nohup gunicorn app:app > log.txt &
echo $! >> pid.txt
