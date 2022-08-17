import json
from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/new_eq_data_30_days.json'

with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    mags.append(eq_dict['properties']['mag'])
    hover_texts.append(eq_dict['properties']['title'])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [4 * mag for mag in mags],
        'color': mags,
        'colorscale': 'hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
