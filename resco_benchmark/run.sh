#!/bin/bash
export LIBSUMO_AS_TRACI=1
export TFM_RESCO_PWD=$PWD
export TFM_RESCO_LOG_DIR="$PWD/results/"

export TFM_RESCO_EPS=1500
export TFM_RESCO_TR=3

# HOW TO RUN: train/train.sh AGENT TRIES

TRIES_COUNTER=0
while [ $TRIES_COUNTER -le $((TFM_RESCO_TR - 1)) ]
do
    if [ $TRIES_COUNTER -ne 0 ]; then # Because we already ran one run
        train/train.sh IDQN $TRIES_COUNTER
        train/train.sh IPPO $TRIES_COUNTER
    fi

    train/train.sh MPLight $TRIES_COUNTER
    train/train.sh MPLightFULL $TRIES_COUNTER
    train/train.sh FMA2C $TRIES_COUNTER
    train/train.sh FMA2CFULL $TRIES_COUNTER

    if [ $TRIES_COUNTER -ne 0 ]; then # Because we already ran one run
        train/train.sh STOCHASTIC $TRIES_COUNTER
	    train/train.sh MAXWAVE $TRIES_COUNTER
        train/train.sh MAXPRESSURE $TRIES_COUNTER
    fi

    
    echo RUN $((++TRIES_COUNTER))/$TFM_RESCO_TR FINISHED
done

