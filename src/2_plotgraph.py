import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
import argparse

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, help='The name of the file to be imported')
parser.add_argument('-o', '--output', type=str, help='The name of the `png` file')

args = parser.parse_args()

def read_data(file_name):
    # Read the data
    data = pd.read_csv(file_name)
    return data

def add_time_column(data):
    # Ask user the time interval
    t_interval = float(input("INFO: Enter the time interval of the exported trajectory (in ns): "))

    # Add a new column called 'Time' to the dataframe
    data['time'] = data['Frame'] * t_interval
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
    rcParams['axes.titleweight'] = 'normal'
    rcParams['axes.titlesize'] = 18

    # Axes settings
    rcParams['axes.labelweight'] = 'normal'
    rcParams['xtick.labelsize'] = 12
    rcParams['ytick.labelsize'] = 12
    rcParams['axes.labelsize'] = 16
    rcParams['xtick.direction'] = 'in'

    rcParams['ytick.direction'] = 'in'

    # Legend font settings
    rcParams['legend.fontsize'] = 11
    rcParams['legend.title_fontsize'] = 12
    rcParams['legend.frameon'] = True

def plot_and_save(data, output_prefix):
    # Drop the `Frame` column
    data = data.drop(columns=['Frame'])
    color_list = ['black', 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']

    for column in data.columns:
        if column == 'time':
            continue # Skip the `time` to avoid plotting it  
        elif column == '#':
            continue

        plt.figure(figsize=(4, 3))

        # change the color of the graph by looping through the color_list
        plt.plot(data['time'], data[column], label=column, color=color_list[data.columns.get_loc(column)])
        plt.xlabel('Time (ns)', color = color_list[data.columns.get_loc(column)])

        # Set the y-axis label
        if column=="ChillPlus.counts.HYDRATE":
            plt.ylabel("Hydrate counts", color = color_list[data.columns.get_loc(column)])
        elif column=="ChillPlus.counts.HEXAGONAL_ICE":
            plt.ylabel("Hexagonal ice counts", color = color_list[data.columns.get_loc(column)])
        elif column=="ChillPlus.counts.CUBIC_ICE":
            plt.ylabel("Cubic ice counts", color = color_list[data.columns.get_loc(column)])
        elif column=="ChillPlus.counts.INTERFACIAL_HYDRATE":
            plt.ylabel("Interfacial hydrate counts", color = color_list[data.columns.get_loc(column)])
        elif column=="ChillPlus.counts.INTERFACIAL_ICE":
            plt.ylabel("Interfacial ice counts", color = color_list[data.columns.get_loc(column)])
        elif column=="ChillPlus.counts.OTHERS":
            plt.ylabel("Others", color = color_list[data.columns.get_loc(column)])
        else:
            pass

        # xlim
        plt.xlim(0, data['time'].max())

        # Ticks
        plt.tick_params(axis='x', colors=color_list[data.columns.get_loc(column)])
        plt.tick_params(axis='y', colors=color_list[data.columns.get_loc(column)])
        plt.tick_params(axis='x', which='minor', colors=color_list[data.columns.get_loc(column)])
        plt.tick_params(axis='y', which='minor', colors=color_list[data.columns.get_loc(column)])

        # Color spines
        ax = plt.gca()
        for spine in ax.spines.values():
            spine.set_edgecolor(color_list[data.columns.get_loc(column)])

        plt.tight_layout()
        plt.savefig(f'{output_prefix}_{column}.png', dpi=300, bbox_inches='tight')
        plt.close()

        print(f"INFO: `{column}` has been plotted and saved.")

if __name__ == '__main__':
    input_file = args.input
    output_prefix = args.output

    # Read and process data
    data = read_data(input_file)
    data = add_time_column(data)
    set_rcparams()

    # Plot and save graphs
    plot_and_save(data, output_prefix)
