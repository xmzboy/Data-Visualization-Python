import requests
from plotly import offline

API_TOKEN = 'YOUR_TOKEN'
USER = 'YOUR_USERNAME'
url = 'https://api.github.com/user/repos'
headers = {'Accept', 'application/vnd.github.v3+json'}


r = requests.get(url, auth=(USER, API_TOKEN))
print(f"Status code: {r.status_code}")
response_dict = r.json()

repo_names, size, labels = [], [], []
print(f"Repositories returned: {len(response_dict)}")
repo_dict = response_dict[0]

print("\nSelected information about each repository:")
for repo_dict in response_dict:
    repo_names.append(f"<a href= '{repo_dict['html_url']}'>{repo_dict['name']}")
    size.append(repo_dict['size'])
    labels.append(f"Description: {repo_dict['description']}<br />"
                  f"Created: {repo_dict['created_at']}<br />"
                  f"Updated: {repo_dict['updated_at']}")

data = [{
    'type': 'bar',
    'x': repo_names,
    'y': size,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 150, 150)',
        'line': {'width': 5, 'color': 'black'}
    },
    'opacity': 0.8
}]

my_layout = {
    'title': 'Size of my projects on GitHub',
    'titlefont': {'size': 28, 'family': 'Roboto'},
    'xaxis': {'title': 'Repository',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
    'yaxis': {'title': 'Size',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14}
              },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_rep.html')
