#!/bin/bash
AGENT=$1
cd utils

python readCSV.py
python readXML.py

cd ../

# commit
train/git.sh $AGENT

