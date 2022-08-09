import csv
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

filename = 'data/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brighs = [], [], []
    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        brighs.append(row[2])


data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global fires')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')


