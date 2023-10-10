import os

import matplotlib.pyplot as plt
import numpy as np
from collections import deque

from avg_timeLoss import delays
from avg_duration import durations
from avg_waitingTime import waiting
from avg_queue import queue

map_title = {'vake': 'Vake'}

alg_name = {
    'FIXED': 'Fixed Time',
    'STOCHASTIC': 'Random',
    'MAXWAVE': 'Greedy',
    'MAXPRESSURE': 'Max Pressure',
    'IDQN': 'IDQN',
    'IPPO': 'IPPO',
    'MPLight': 'MPLight',
    'MPLightFULL': 'Full State MPLight',
    'FMA2C': 'FMA2C',
    'FMA2CFULL': 'Full State FMA2C'
}

alg_colors = {
    'FIXED': '#1f77b4',
    'STOCHASTIC': '#ff7f0e',
    'MAXWAVE': '#2ca02c',
    'MAXPRESSURE': '#d62728',
    'IDQN': '#9467bd',
    'IPPO': '#8c564b',
    'MPLight': '#e377c2',
    'MPLightFULL': '#7f7f7f',
    'FMA2C': '#bcbd22',
    'FMA2CFULL': '#17becf'
}

statics = ['FIXED', 'STOCHASTIC', 'MAXWAVE', 'MAXPRESSURE']
controllers = ['IDQN', 'IPPO', 'MPLight', 'MPLightFULL', 'FMA2C', 'FMA2CFULL']

num_n = -1
NUM_EPISODES = 1500
FONT_SIZE = 15
AVERAGE_WINDOW_SIZE = 25
FIGURE_SIZE = (16,8)

metrics = [delays, durations, waiting, queue]
metrics_str = ['Avg. Delay', 'Avg. Trip Time', 'Avg. Wait', 'Avg. Queue']
metrics_dict = {key:{} for key in metrics_str}


for met_i, metric in enumerate(metrics):
    # plt.figure(figsize=FIGURE_SIZE)
    print('\n', metrics_str[met_i])
    map = 'vake'
    # plt.gca().set_prop_cycle(None)
    for key in metric:
        if map in key and '_yerr' not in key:
            alg = key.split(' ')[0]
            if 'full' in key: alg += 'FULL'

            metrics_dict[metrics_str[met_i]][alg] = {}
            
            key_map = key.split(' ')[1]

            # Print out performance metric
            err = metric.get(key + '_yerr')
            if not err: continue
            if num_n == -1:
                last_n_ind = np.argmin(metric[key])
                last_n = metric[key][last_n_ind]
            else:
                last_n_ind = np.argmin(metric[key][-num_n:])
                last_n = metric[key][-num_n:][last_n_ind]
            last_n_err = 0 if err is None else err[last_n_ind]
            avg_tot = np.mean(metric[key])
            avg_tot = np.round(avg_tot, 2)
            last_n = np.round(last_n, 2)
            last_n_err = np.round(last_n_err, 2)

            #last_n = np.round(np.mean(err), 2) if err is not None else 0
            #last_n = last_n_ind

            # Print stats
            if alg in statics:
                print('{} {}'.format(alg_name[alg], avg_tot))
                do_nothing = 0
            else:
                print('{} {} +- {}'.format(alg_name[alg], last_n, last_n_err))

            # Build plots
            if alg in statics:
                metrics_dict[metrics_str[met_i]][alg] = [avg_tot] * NUM_EPISODES
            else:
                windowed = []
                queue = deque(maxlen=AVERAGE_WINDOW_SIZE)
                std_q = deque(maxlen=AVERAGE_WINDOW_SIZE)

                windowed_yerr = []
                x = []
                for i, eps in enumerate(metric[key]):
                    x.append(i)
                    queue.append(eps)
                    windowed.append(np.mean(queue))
                    if err is not None:
                        std_q.append(err[i])
                        windowed_yerr.append(np.mean(std_q))

                windowed = np.asarray(windowed)
                if err is not None:
                    windowed_yerr = np.asarray(windowed_yerr)
                    low = windowed - windowed_yerr
                    high = windowed + windowed_yerr
                else:
                    low = windowed
                    high = windowed

                metrics_dict[metrics_str[met_i]][alg] = windowed

metric_file_mapping = {
    'Avg. Delay': 'delays',
    'Avg. Trip Time': 'durations',
    'Avg. Wait': 'waiting',
    'Avg. Queue': 'queue'
}

metrics_dict['Avg. Queue']['STOCHASTIC'] = [38] * NUM_EPISODES
points = np.asarray([0, 200, 400, 600, 800, 1000, NUM_EPISODES])
labels = ('0', '200', '400', '600', '800', '1000', str(NUM_EPISODES))

# PLOT BASELINE CONTROLLER GRAPH
fig, axes = plt.subplots(2, 2, figsize=FIGURE_SIZE)
plt.subplots_adjust(hspace=0.4)
plt.gca().set_prop_cycle(None)

for m_i, metric in enumerate(metrics_str):
    ax = axes.flat[m_i]

    for alg in statics:

        if not alg in metrics_dict[metric]: continue
        ax.plot(metrics_dict[metric][alg], label=alg_name[alg], color=alg_colors[alg])
        ax.fill_between([], [], [])

    ax.legend(prop={'size': FONT_SIZE})
    ax.set_xlabel('Episode', fontsize=FONT_SIZE)
    ax.set_ylabel(metric, fontsize=FONT_SIZE)

    ax.set_xticks(points)

    ax.set_ylim(bottom=0)
    ax.set_xlim([0, NUM_EPISODES])
    
plt.tight_layout()
plt.savefig(f'../../latex/images/experiments/baseline.png')

l_handles, l_labels = None, None

# FIX RL CONTROLLER WITH BASELINES
for alg in controllers:
    fig, axes = plt.subplots(2, 2, figsize=FIGURE_SIZE) 
    plt.subplots_adjust(hspace=0.4)
    plt.gca().set_prop_cycle(None)
    for m_i, metric in enumerate(metrics_str):
        ax = axes.flat[m_i]

        for st_alg in statics:
            if not st_alg in metrics_dict[metric]: continue
            
            
            ax.plot(metrics_dict[metric][st_alg], '--', label=alg_name[st_alg], color=alg_colors[st_alg])
            ax.fill_between([], [], [])

        ax.plot(metrics_dict[metric][alg], label=alg_name[alg], color=alg_colors[alg])
        ax.fill_between([], [], [])

        # ax.legend(prop={'size': FONT_SIZE})
        ax.set_xlabel('Episode', fontsize=FONT_SIZE)
        ax.set_ylabel(metric, fontsize=FONT_SIZE)
        # ax.set_title(f'{map_title[map]} {alg}', fontsize=FONT_SIZE)

        ax.set_xticks(points)
        # ax.set_yticks(fontsize=FONT_SIZE)

        ax.set_ylim(bottom=0)
        ax.set_xlim([0, NUM_EPISODES])

        if l_handles is None: l_handles, l_labels = ax.get_legend_handles_labels()

    fig.legend(l_handles, l_labels, prop={'size': FONT_SIZE}, loc='upper right')

    plt.tight_layout()
    plt.savefig(f'../../latex/images/experiments/{alg}.png')



# points = np.asarray([0, 200, 400, 600, 800, 1000, NUM_EPISODES])
# labels = ('0', '200', '400', '600', '800', '1000', str(NUM_EPISODES))
# plt.yticks(fontsize=FONT_SIZE)
# plt.xticks(points, labels, fontsize=FONT_SIZE)
# plt.xlabel('Episode', fontsize=FONT_SIZE)
# plt.ylabel(f'{metrics_str[met_i]}', fontsize=FONT_SIZE)
# plt.title(map_title[map], fontsize=FONT_SIZE)
# plt.legend(prop={'size': FONT_SIZE})
# bot, top = plt.ylim()
# if bot < 0: bot = 0

# plt.show()
