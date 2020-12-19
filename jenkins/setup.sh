#!/bin/bash
virtualenv --python=python3 env --no-site-packages
. env/bin/activate
pip install -r requirements.txt

export FLASK_APP=app.py
flask db migrate
flask db upgrade