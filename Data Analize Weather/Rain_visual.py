import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get dates, and rainfall amounts from this file.
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(current_date)
        rains.append(rain)

    # Plot the high and low temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rains, c='red')
    # Format plot.
    plt.title("Daily rainfall amounts - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Rainfall amounts", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
