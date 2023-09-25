#/bin/bash
AGENT=$1

git pull
git add --ignore-errors utils/*
git commit -m "FROM SHELL. AGENT: $AGENT, EPS: $TFM_RESCO_EPS, TRIES: $TFM_RESCO_TR"
git push