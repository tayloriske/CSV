import csv
from datetime import datetime

infile = open("death_valley_2018_simple.csv", "r")

csvfile = csv.reader(infile, delimiter = ",")

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    print(index,column_header)

highs = []
dates = []
lows = []

for line in csvfile:
    try:
        high = int(line[4])
        low = int(line[5])
        date = datetime.strptime(line[2], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c= "blue")

plt.fill_between(dates,highs,lows, facecolor="blue", alpha=0.1)

plt.title("Daily High Temperatures - 2018\nDeath Valley", fontsize = 16)
plt.xlabel("July 2018", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize=16)

fig.autofmt_xdate()

plt.show()
