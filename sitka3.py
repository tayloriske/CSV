import csv
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")

csvfile = csv.reader(infile, delimiter = ",")

header_row = next(csvfile)

#print(header_row)

for index, column_header in enumerate(header_row):
    print(index,column_header)

highs = []
dates = []
lows = []

for line in csvfile:
    highs.append(int(line[5]))
    lows.append(int(line[6]))
    date = datetime.strptime(line[2], "%Y-%m-%d")
    dates.append(date)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c= "blue")

plt.fill_between(dates,highs,lows, facecolor="blue", alpha=0.1)

plt.title("Daily High Temperatures - 2018", fontsize = 16)
plt.xlabel("July 2018", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", which = "major", labelsize=16)

fig.autofmt_xdate()

plt.show()


plt.subplot(2, 1, 1)
# (2 rows, 1 column, index value)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()