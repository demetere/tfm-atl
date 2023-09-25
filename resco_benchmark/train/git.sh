#/bin/bash
git pull
git add --ignore-errors utils/*
git commit -m "updated results for $1, eps: $TFM_RESCO_EPS"
git push