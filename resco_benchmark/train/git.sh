#/bin/bash
TRY=$1
AGENT=$2

git pull
git add --ignore-errors utils/*
git commit -m "FROM SHELL. AGENT: $AGENT, EPS: $TFM_RESCO_EPS, TRY: $TRY"
git push