#/bin/bash
AGENT=$1

git pull
git add --ignore-errors utils/*
git commit -m "updated results for $AGENT, eps: $TFM_RESCO_EPS"
git push