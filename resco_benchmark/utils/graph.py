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
    'MPLight': 'MPLight',
    'MPLightFULL': 'Full State MPLight',
    'FMA2C': 'FMA2C',
    'FMA2CFULL': 'Full State FMA2C',
    'IPPO': 'IPPO'
}

alg_colors = {
    'FIXED': 'b',
    'STOCHASTIC': 'g',
    'MAXWAVE': 'r',
    'MAXPRESSURE': 'c',
    'IDQN': 'm',
    'IPPO': 'orange',
    'MPLight': 'y',
    'MPLightFULL': 'y',
    'FMA2C': 'pink',
    'FMA2CFULL': 'pink'
}

statics = ['MAXPRESSURE', 'STOCHASTIC', 'MAXWAVE', 'FIXED']

num_n = -1
NUM_EPISODES = 1500
FONT_SIZE = 15
AVERAGE_WINDOW_SIZE = 25
FIGURE_SIZE = (16,8)

metrics = [delays, durations, waiting, queue]
metrics_str = ['Avg. Delay', 'Avg. Trip Time', 'Avg. Wait', 'Avg. Queue']

chart = {
    'IDQN': {
        'Avg. Delay': [],
        'Avg. Wait': [],
        'Avg. Queue': [],
        'Avg. Trip Time': []
    },
    'IPPO': {
        'Avg. Delay': [],
        'Avg. Wait': [],
        'Avg. Queue': [],
        'Avg. Trip Time': []
    },
    'MPLight': {
        'Avg. Delay': [],
        'Avg. Wait': [],
        'Avg. Queue': [],
        'Avg. Trip Time': []
    },
    'FMA2C': {
        'Avg. Delay': [],
        'Avg. Wait': [],
        'Avg. Queue': [],
        'Avg. Trip Time': []
    },
    'Full State MPLight': {
        'Avg. Delay': [],
        'Avg. Wait': [],
        'Avg. Queue': [],
        'Avg. Trip Time': []
    },
}

fig, axes = plt.subplots(2, 2, figsize=FIGURE_SIZE) 
plt.subplots_adjust(hspace=0.4)
plt.gca().set_prop_cycle(None)

l_handles, l_labels = None, None

for met_i, metric in enumerate(metrics):
    ax = axes.flat[met_i]
    print('\n', metrics_str[met_i])
    map = 'vake'
    for key in metric:
        if map in key and '_yerr' not in key:
            alg = key.split(' ')[0]
            if 'full' in key: alg += 'FULL'
            
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
                ax.plot([avg_tot]*NUM_EPISODES, '--', label=alg_name[alg], color=alg_colors[alg])
                ax.fill_between([], [], [])      # Advance color cycle
            # elif not('FMA2C' in alg or 'IPPO' in alg):
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

                ax.plot(windowed, label=alg_name[alg])
                ax.fill_between(x, low, high, alpha=0.4)

    points = np.asarray([0, 200, 400, 600, 800, 1000, NUM_EPISODES])
    labels = ('0', '200', '400', '600', '800', '1000', str(NUM_EPISODES))
    
    # ax.legend(prop={'size': FONT_SIZE})
    ax.set_xlabel('Episode', fontsize=FONT_SIZE)
    ax.set_ylabel(f'{metrics_str[met_i]}', fontsize=FONT_SIZE)
    ax.set_xticks(points)
    ax.set_ylim(bottom=0)
    ax.set_xlim([0, NUM_EPISODES])

    if l_handles is None: l_handles, l_labels = ax.get_legend_handles_labels()

# plt.savefig(f'../../latex/images/experiments/all.png')
# Add legend outside of the subplots

fig.legend(l_handles, l_labels, prop={'size': FONT_SIZE}, loc='upper right')

plt.savefig(f'../../latex/images/experiments/all.png')
# plt.show()
