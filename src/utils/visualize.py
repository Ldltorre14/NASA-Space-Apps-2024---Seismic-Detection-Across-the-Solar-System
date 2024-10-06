import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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


def visualizeVelocityOverTime(data, time_format='%Y-%m-%d %H:%M:%S', interval=2):
     # Create a plot of velocity over time
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot velocity against time
    ax.plot(data['time_abs(%Y-%m-%dT%H:%M:%S.%f)'], data['velocity(m/s)'], label='Velocity (m/s)')
    
    # Set the title and labels
    ax.set_title("Velocity over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Velocity (m/s)")
    
    # Format the x-axis dates
    locator = mdates.HourLocator(interval=interval)
    ax.xaxis.set_major_locator(locator=locator)
    
    # Auto-rotate the x-axis labels for better readability
    fig.autofmt_xdate()

    plt.show()

def visualizeRollingCorrelationTimeVelocity(data, window=50000):
    rolling_corr = data['velocity(m/s)'].rolling(window=window).corr()
    plt.plot(rolling_corr)
    plt.title('Rolling Correlation (Window = {})'.format(window))
    plt.show()