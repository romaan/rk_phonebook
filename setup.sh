#!/bin/bash

sudo apt-get install -y virtualenv
virtualenv /tmp/rk_assignment
source /tmp/rk_assignment/bin/activate
pip install -r requirements.txt
python -m unittest discover -v