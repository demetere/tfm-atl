export LIBSUMO_AS_TRACI=1
export TFM_RESCO_PWD=$PWD
export TFM_RESCO_LOG_DIR="$PWD/results/"

export TFM_RESCO_EPS=1500
export TFM_RESCO_TR=2

# HOW TO RUN: train/train.sh AGENT TRIES

TRIES_COUNTER=0
while [ $TRIES_COUNTER -le $((TFM_RESCO_TR - 1)) ]
do
    # train/train.sh STOCHASTIC $TRIES_COUNTER
    # train/train.sh MAXWAVE $TRIES_COUNTER
    # train/train.sh MAXPRESSURE $TRIES_COUNTER
    # train/train.sh IDQN $TRIES_COUNTER
    # train/train.sh IPPO $TRIES_COUNTER
    # train/train.sh MPLIGHT $TRIES_COUNTER
    # train/train.sh MPLIGHTFULL $TRIES_COUNTER
    # train/train.sh FMA2C $TRIES_COUNTER
    # train/train.sh FMA2CFULL $TRIES_COUNTER
    echo "RUN $((++TRIES_COUNTER))/$TFM_RESCO_TR FINISHED"
done

