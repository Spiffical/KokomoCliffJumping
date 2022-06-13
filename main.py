import matplotlib.pyplot as plt
import seaborn as sns
from data import *
from physics import *

kokomo_runtime = 3.583  # minutes


def autolabel(plot, bar_labels):
    for idx, rect in enumerate(plot):
        bar_height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., bar_height+0.1,
                bar_labels[idx],
                ha='center', va='bottom', rotation=0,
                c='black')


if __name__ == '__main__':
    # Calculate values of interest for each cliff
    for cliff in cliffs:
        host = cliffs[cliff]['host']
        height = cliffs[cliff]['height']
        m_host = solar_system_objects[host]['mass']
        r_host = solar_system_objects[host]['radius']
        start_height = r_host + height
        total_time = freefall_time(start_height, r_host, m_host)
        impact_speed = speed(start_height, r_host, m_host)
        cliffs[cliff]['freefall_time_m'] = total_time / 60.
        cliffs[cliff]['impact_speed_kph'] = impact_speed * 3.6

    # Collect data
    heights = np.asarray([cliffs[cliff]['height'] for cliff in cliffs])
    freefall_times = np.asarray([cliffs[cliff]['freefall_time_m'] for cliff in cliffs])
    final_speeds = np.asarray([cliffs[cliff]['impact_speed_kph'] for cliff in cliffs])
    num_kokomos = np.asarray(freefall_times) / kokomo_runtime
    cliff_names = np.asarray(list(cliffs.keys()))

    # Keep only those objects where n_kokomo > 1
    gt1_kokomos = num_kokomos > 1
    num_kokomos = num_kokomos[gt1_kokomos]
    heights = heights[gt1_kokomos]
    freefall_times = freefall_times[gt1_kokomos]
    final_speeds = final_speeds[gt1_kokomos]
    cliff_names = cliff_names[gt1_kokomos]

    # Plot results
    sns.set_style('darkgrid')  # darkgrid, white grid, dark, white and ticks
    plt.rc('axes', titlesize=18)  # fontsize of the axes title
    plt.rc('axes', labelsize=18)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=13)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=17)  # fontsize of the tick labels
    plt.rc('legend', fontsize=13)  # legend fontsize
    plt.rc('font', size=13)  # controls default text sizes
    fig, ax = plt.subplots(1, 1, figsize=(18, 8))
    #colors = sns.color_palette('pastel')
    #color = colors[:len(num_kokomos)]
    color = 'white'
    x_vals = np.arange(len(num_kokomos))
    #x_vals = np.asarray(heights)/1000
    bar_plot = ax.bar(x_vals, sorted(num_kokomos), width=1., color=color, edgecolor='black')
    ax.axes.xaxis.set_ticklabels([])
    title_text = 'How many times could you listen to Kokomo while \nfalling off of various ' \
                 'cliffs in the solar system?'
    ax.set(title=title_text, ylabel='Number of Kokomos',
           ylim=(0, 4.5))
    labels_cliff_names = [x for _, x in sorted(zip(num_kokomos, cliff_names))]
    labels_cliff_heights = [x for _, x in sorted(zip(num_kokomos, heights))]
    labels_impact_speeds = [x for _, x in sorted(zip(num_kokomos, final_speeds))]
    labels = [f'{labels_cliff_names[j]}\n'
              f'{labels_cliff_heights[j]/1000}km\n'
              f'{labels_impact_speeds[j]:.1f}km/h'
              for j in range(len(labels_cliff_names))]
    autolabel(bar_plot, labels)
    plt.savefig('cliffjumping_scaffold.png')
