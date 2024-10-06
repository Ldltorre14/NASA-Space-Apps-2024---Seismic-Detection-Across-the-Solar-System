import pandas as pd
import matplotlib.pyplot as plt
import constants.consts as cs



def visualizeDf(data):
    print(data.info())
    #print(data.head())
    #print(data.describe())

    print(f"Minimun Velocity: {data['velocity(m/s)'].min()}")
    print(f"Maximum Velocity: {data['velocity(m/s)'].max()}")
    print(f"Median Velocity: {data['velocity(m/s)'].median()}")
    print(f"Mean Velocity: {data['velocity(m/s)'].mean()}")
    print(f"Mode Velocity: {data['velocity(m/s)'].mode()}")

    plt.boxplot(data['velocity(m/s)'])
    plt.show()