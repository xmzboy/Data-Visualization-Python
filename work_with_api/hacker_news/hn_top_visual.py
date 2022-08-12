from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []
comments, labels, links = [], [], []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"ID: {submission_id}\t status: {r.status_code}")
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://hacker-news.firebaseio.com/v0/item/{submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    comments.append(int(submission_dict['comments']))
    links.append(f"<a href = '{submission_dict['hn_link']}'> {submission_dict['title']}")
    labels.append(submission_dict['title'])

data = [{
    'type': 'bar',
    'x': links,
    'y': comments,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(118, 196, 168)',
        'line': {'width': 3, 'color': 'black'}
    }
}]

my_layout = {
    'title': 'Hacker News Top Stories',
    'xaxis': {'title': 'Stories'},
    'yaxis': {'title': 'Comments'},
}

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='hn_top_stories.html')

