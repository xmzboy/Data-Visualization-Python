import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for i in range(len(header_row)):
        if header_row[i] == 'TMAX':
            tmax = i
        elif header_row[i] == 'TMIN':
            tmin = i
    highs, lows, prcps = [], [], []
    dates = []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = (int(row[tmax]) - 32) / 1.8
            low = (int(row[tmin]) - 32) / 1.8
            prcp = float(row[3])
        except:
            pass
        else:
            prcps.append(prcp)
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.7, linewidth=2)
ax.plot(dates, lows, alpha=0.7, linewidth=2)
ax.plot(dates, prcps, c='green', linewidth=2)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily temperatures - 2018', fontsize=24)
plt.xlabel('', fontsize=14)
plt.ylabel('Temperature | Precipitation', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
fig.autofmt_xdate()

plt.show()
