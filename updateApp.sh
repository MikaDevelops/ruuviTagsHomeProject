#!/bin/bash

git pull
python -m unittest discover -p "*_test.py"
