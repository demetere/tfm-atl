export LIBSUMO_AS_TRACI=1
export TFM_RESCO_PWD=~/Projects/mai/traffic-control/tfm-atl/resco_benchmark
export TFM_RESCO_LOG_DIR=~/Projects/mai/traffic-control/tfm-atl/resco_benchmark/results/


export TFM_RESCO_EPS=5
TFM_RESCO_TR=1

# HOW TO RUN: train/train.sh AGENT TRIES

# train/train.sh STOCHASTIC 1
# train/train.sh MAXWAVE 1
# train/train.sh MAXPRESSURE 1
# train/train.sh IDQN $TFM_RESCO_TR
# train/train.sh IPPO $TFM_RESCO_TR
# train/train.sh MPLIGHT $TFM_RESCO_TR
# train/train.sh MPLIGHTFULL $TFM_RESCO_TR
# train/train.sh FMA2C $TFM_RESCO_TR
# train/train.sh FMA2CFULL $TFM_RESCO_TR