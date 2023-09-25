#!/bin/bash
AGENT_NAME=$1
TRIES=$2

TRIES_COUNTER=0
while [ $TRIES_COUNTER -le $((TRIES - 1)) ]
do
    python main.py \
        --agent $AGENT_NAME \
        --map vake \
        --libsumo 1 \
        --tr $TRIES_COUNTER \
        --eps $TFM_RESCO_EPS \
        --pwd $TFM_RESCO_PWD \
        --log_dir $TFM_RESCO_LOG_DIR
    echo RUN $((++TRIES_COUNTER))/$TRIES FINISHED
done

train/analyses.sh $AGENT_NAME