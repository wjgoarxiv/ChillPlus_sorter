import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import argparse

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, help='The name of the file to be imported')
parser.add_argument('-o', '--output', type=str, help='The name of the output png file')
args = parser.parse_args()

def read_data(file_name):
    # Read the data from the CSV file
    data = pd.read_csv(file_name)
    return data

def add_time_column(data):
    # Add a column for the time in ns. Note that it is the column that divided the `frame` column by 10
    data['time'] = data['Frame']/10
    return data

def reset_time_to_zero(data):
    # In this code block, we will find the time when the hydrate count is maximum. And then, reset the time to zero at that point.
    # Find the maximum hydrate count
    max_hydrate_count = data['ChillPlus.counts.HYDRATE'].max()

    # Find the time when the hydrate count is maximum
    max_hydrate_time = data.loc[data['ChillPlus.counts.HYDRATE'] == max_hydrate_count, 'time'].iloc[0]

    # Reset the time to zero at the point when the hydrate count is maximum
    data['time'] = data['time'] - max_hydrate_time

    # Delete the rows if time < 0
    data = data[data['time'] >= 0]
    return data

def set_rcparams():
    # Rcparams settings
    rcParams['font.family'] = 'sans-serif'

    # Check whether Arial or SF Pro Display are installed in the computer
    try:
        rcParams['font.sans-serif'] = ['SF Pro Display']
    except:
        try:
            rcParams['font.sans-serif'] = ['Arial']
        except:
            print("ERROR Note that Arial and SF Pro are not installed in the computer. The program will use the default font.")
            pass

    # Label should be far away from the axes
    rcParams['axes.labelpad'] = 8
    rcParams['xtick.major.pad'] = 7
    rcParams['ytick.major.pad'] = 7

    # Add minor ticks
    rcParams['xtick.minor.visible'] = True
    rcParams['ytick.minor.visible'] = True

    # Tick width
    rcParams['xtick.major.width'] = 1
    rcParams['ytick.major.width'] = 1
    rcParams['xtick.minor.width'] = 0.5
    rcParams['ytick.minor.width'] = 0.5

    # Tick length
    rcParams['xtick.major.size'] = 5
    rcParams['ytick.major.size'] = 5
    rcParams['xtick.minor.size'] = 3
    rcParams['ytick.minor.size'] = 3

    # Tick color
    rcParams['xtick.color'] = 'black'
    rcParams['ytick.color'] = 'black'

    rcParams['font.size'] = 14
    rcParams['axes.titlepad'] = 10
    rcParams['axes.titleweight'] = 'bold'
    rcParams['axes.titlesize'] = 18

    # Axes settings
    rcParams['axes.labelweight'] = 'bold'
    rcParams['xtick.labelsize'] = 12
    rcParams['ytick.labelsize'] = 12
    rcParams['axes.labelsize'] = 16
    rcParams['xtick.direction'] = 'in'

    rcParams['ytick.direction'] = 'in'

    # Legend font settings
    rcParams['legend.fontsize'] = 11
    rcParams['legend.title_fontsize'] = 12
    rcParams['legend.frameon'] = True

def plot_graph(x, y, ax, color, label):
    # Plot the data
    ax.plot(x, y, label=label, color=color)

    # Set the frame color
    ax.spines['bottom'].set_color(color)
    ax.spines['top'].set_color(color)
    ax.spines['left'].set_color(color)
    ax.spines['right'].set_color(color)

    # Tick color changing
    ax.tick_params(axis='x', colors=color)
    ax.tick_params(axis='y', colors=color)

    # Minor tick color changing
    ax.tick_params(axis='x', which='minor', colors=color)
    ax.tick_params(axis='y', which='minor', colors=color)

    # Set the x limit
    ax.set_xlim(0, )

def main():
    args = parser.parse_args()
    input_file = args.input 
    data = read_data(input_file)
    data = add_time_column(data)
    data = reset_time_to_zero(data)
    set_rcparams()

    # `Frame` is the x data.
    # y1 = `ChillPlus.counts.HYDRATE`
    # y2 = `ChillPlus.counts.HEXAGONAL_ICE`
    # y3 = `ChillPlus.counts.INTERFACIAL_HYDRATE`
    # y4 = `ChillPlus.counts.INTERFACIAL_ICE`

    # And all the other columns are y data.
    # Let's plot them in each subplots.

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    plot_graph(data['time'], data['ChillPlus.counts.HYDRATE'], axes[0, 0], 'tab:orange', '$N_{Hydrate}$')
    plot_graph(data['time'], data['ChillPlus.counts.HEXAGONAL_ICE'], axes[0, 1], 'tab:blue', 'HEXAGONAL_ICE')
    plot_graph(data['time'], data['ChillPlus.counts.INTERFACIAL_HYDRATE'], axes[1, 0], 'tab:purple', 'INTERFACIAL_HYDRATE')
    plot_graph(data['time'], data['ChillPlus.counts.INTERFACIAL_ICE'], axes[1, 1], 'tab:green', 'INTERFACIAL_ICE')

    # Set the title
    axes[0, 0].set_title('Hydrates', color = 'tab:orange')
    axes[0, 1].set_title('Hexagonal ices', color = 'tab:blue')
    axes[1, 0].set_title('Interfacial hydrates', color = 'tab:purple')
    axes[1, 1].set_title('Interfacial ices', color = 'tab:green')

    # Set the x label
    axes[0, 0].set_xlabel('Time (ns)', color = 'tab:orange')
    axes[0, 1].set_xlabel('Time (ns)', color = 'tab:blue')
    axes[1, 0].set_xlabel('Time (ns)', color = 'tab:purple')
    axes[1, 1].set_xlabel('Time (ns)', color = 'tab:green')

    # Set the y label
    axes[0, 0].set_ylabel('Counts', color = 'tab:orange', labelpad=12)
    axes[0, 1].set_ylabel('Counts', color = 'tab:blue')
    axes[1, 0].set_ylabel('Counts', color = 'tab:purple')
    axes[1, 1].set_ylabel('Counts', color = 'tab:green')

    # Tick color changing
    axes[0, 0].tick_params(axis='x', colors='tab:orange')
    axes[0, 0].tick_params(axis='y', colors='tab:orange')

    axes[0, 1].tick_params(axis='x', colors='tab:blue')
    axes[0, 1].tick_params(axis='y', colors='tab:blue')

    axes[1, 0].tick_params(axis='x', colors='tab:purple')
    axes[1, 0].tick_params(axis='y', colors='tab:purple')

    axes[1, 1].tick_params(axis='x', colors='tab:green')
    axes[1, 1].tick_params(axis='y', colors='tab:green')

    # Minor tick color changing
    axes[0, 0].tick_params(axis='x', which='minor', colors='tab:orange')
    axes[0, 0].tick_params(axis='y', which='minor', colors='tab:orange')

    axes[0, 1].tick_params(axis='x', which='minor', colors='tab:blue')
    axes[0, 1].tick_params(axis='y', which='minor', colors='tab:blue')

    axes[1, 0].tick_params(axis='x', which='minor', colors='tab:purple')
    axes[1, 0].tick_params(axis='y', which='minor', colors='tab:purple')

    axes[1, 1].tick_params(axis='x', which='minor', colors='tab:green')
    axes[1, 1].tick_params(axis='y', which='minor', colors='tab:green')

    # Set legend
    axes[0, 0].legend(loc='upper right')
    axes[0, 1].legend(loc='upper right')
    axes[1, 0].legend(loc='upper right')
    axes[1, 1].legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(args.output, dpi=300)

if __name__ == '__main__':
  main()
