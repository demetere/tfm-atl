export LIBSUMO_AS_TRACI=1

python main.py \
    --agent STOCHASTIC \
    --map vake \
    --eps 100 \
    --libsumo 1 \
    --pwd ~/Projects/mai/traffic-control/tfm-atl/resco_benchmark \
    --log_dir ~/Projects/mai/traffic-control/tfm-atl/resco_benchmark/results/

# python main.py \
#     --agent MAXWAVE \
#     --map vake \
#     --eps 100 \
#     --libsumo 1 \
#     --pwd ~/Projects/mai/traffic-control/tfm-atl/resco_benchmark \
#     --log_dir ~/Projects/mai/traffic-control/tfm-atl/resco_benchmark/results/

# python main.py \
#     --agent MAXPRESSURE \
#     --map vake \
#     --eps 100 \
#     --libsumo 1 \
#     --pwd ~/Projects/mai/traffic-control/tfm-atl/resco_benchmark \
#     --log_dir ~/Projects/mai/traffic-control/tfm-atl/resco_benchmark/results/

# python main.py \
#     --agent IDQN \
#     --map cologne3 \
#     --eps 2 \
#     --libsumo 1 \
#     --pwd ~/Projects/mai/traffic-control/tfm-atl/resco_benchmark \
#     --log_dir ~/Projects/mai/traffic-control/tfm-atl/resco_benchmark/results/