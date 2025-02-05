#!/bin/bash
AGENT_NAME=$1
TRY=$2

python main.py \
    --agent $AGENT_NAME \
    --map vake \
    --libsumo 1 \
    --tr $TRY \
    --eps $TFM_RESCO_EPS \
    --pwd $TFM_RESCO_PWD \
    --log_dir $TFM_RESCO_LOG_DIR

# train/analyses.sh $AGENT_NAME $TRY