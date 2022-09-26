import csv
from datetime import datetime

infile = open("sitka_weather_07-2018_simple.csv", "r")

csvfile = csv.reader(infile, delimiter = ",")

header_row = next(csvfile)

#print(header_row)

for index, column_header in enumerate(header_row):
    print(index,column_header)

highs = []
dates = []

for line in csvfile:
    highs.append(int(line[5]))
    date = datetime.strptime(line[2], "%Y-%m-%d")
    dates.append(date)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.title("Daily High Temperatures, July 2018", fontsize = 16)
plt.xlabel("July 2018", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize=16)

fig.autofmt_xdate()

plt.show()