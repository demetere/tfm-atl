#/bin/bash
AGENT=$1
TRY=$2

git pull
git add --ignore-errors utils/*
git commit -m "FROM SHELL. AGENT: $AGENT, EPS: $TFM_RESCO_EPS, TRY: $TRY"
git push