import csv
from datetime import datetime

############################################

sitka_infile = open("sitka_weather_2018_simple.csv", "r")
sitka_csvfile = csv.reader(sitka_infile, delimiter = ",")
sitka_name = ""
sitka_header_row = next(sitka_csvfile)
sitka_date_index = sitka_header_row.index("DATE")
sitka_highs_index = sitka_header_row.index("TMAX")
sitka_lows_index = sitka_header_row.index("TMIN")
sitka_name_index = sitka_header_row.index("NAME")

sitka_highs, sitka_dates, sitka_lows = [], [], []

for line in sitka_csvfile:
    if not sitka_name:
        sitka_name = line[sitka_name_index]

    date = datetime.strptime(line[sitka_date_index], "%Y-%m-%d")

    try:    
        high = int(line[sitka_highs_index])
        low = int(line[sitka_lows_index])

    except ValueError:
        print(f"Missing data for {date}")

    else:
        sitka_highs.append(int(line[sitka_highs_index]))
        sitka_lows.append(int(line[sitka_lows_index]))
        sitka_dates.append(date)

#############################################

dv_infile = open("death_valley_2018_simple.csv", "r")
dv_csvfile = csv.reader(dv_infile, delimiter = ",")
dv_header_row = next(dv_csvfile)
dv_name = ""
dv_date_index = dv_header_row.index("DATE")
dv_highs_index = dv_header_row.index("TMAX")
dv_lows_index = dv_header_row.index("TMIN")
dv_name_index = dv_header_row.index("NAME")

dv_highs, dv_dates, dv_lows = [], [], []

for line in dv_csvfile:
    if not dv_name:
        dv_name = line[dv_name_index]

    date = datetime.strptime(line[dv_date_index], "%Y-%m-%d")

    try:    
        high = int(line[dv_highs_index])
        low = int(line[dv_lows_index])

    except ValueError:
        print(f"Missing data for {date}")

    else:
        dv_highs.append(int(line[dv_highs_index]))
        dv_lows.append(int(line[dv_lows_index]))
        dv_dates.append(date)

###############################################

import matplotlib.pyplot as plt


plt.subplot(2,1,1)
plt.plot(sitka_dates, sitka_highs, c="red")
plt.plot(sitka_dates, sitka_lows, c= "blue")
plt.fill_between(sitka_dates,sitka_highs,sitka_lows, facecolor="blue", alpha=0.1)
plt.title(sitka_name, fontsize = 16)

plt.subplot(2,1,2)
plt.plot(dv_dates, dv_highs, c="red")
plt.plot(dv_dates, dv_lows, c= "blue")
plt.fill_between(dv_dates,dv_highs,dv_lows, facecolor="blue", alpha=0.1)
plt.title(dv_name, fontsize = 16)

title = "Temperature comparison between " + sitka_name + " and " + dv_name
plt.suptitle(title)

plt.show()