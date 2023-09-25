#!/bin/bash
echo $1
cd utils

python readCSV.py
python readXML.py

cd ../

# commit
train/git.sh $1

