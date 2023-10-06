#/bin/bash
# AGENT=$1
TRY=$1

git pull
git add --ignore-errors utils/*
git commit -m "FROM SHELL. TRY $TRY FOR ALL AGENTS"
git push