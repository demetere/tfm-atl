#!/bin/bash
TRY=$1
AGENT=$2

cd utils

python readCSV.py
python readXML.py

cd ../

# commit
train/git.sh $TRY $AGENT

