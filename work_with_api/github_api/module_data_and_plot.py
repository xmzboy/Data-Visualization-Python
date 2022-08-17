import requests
from plotly import offline


def connection(url):
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    return r


def init_plot(stars, labels, repo_links):
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6
    }]

    my_layout = {
        'title': 'Most-Starred Python Projects on GitHub',
        'titlefont': {'size': 28, 'family': 'Roboto'},
        'xaxis': {'title': 'Repository',
                  'titlefont': {'size': 24},
                  'tickfont': {'size': 14}
                  },
        'yaxis': {'title': 'Stars',
                  'titlefont': {'size': 24},
                  'tickfont': {'size': 14}
                  },
    }
    return data, my_layout


def data_proc(r):
    response_dict = r.json()
    repo_dicts = response_dict['items']
    stars, labels, repo_links = [], [], []

    print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        stars.append(repo_dict['stargazers_count'])
        labels.append(f"Owner: {repo_dict['owner']['login']}<br />"
                      f"Description: {repo_dict['description']}<br />"
                      f"Created: {repo_dict['created_at']}<br />"
                      f"Updated: {repo_dict['updated_at']}")
        repo_links.append(f"<a href='{repo_dict['html_url']}'>{repo_dict['name']}")

    return stars, labels, repo_links


def draw_html(stars, labels, repo_links):
    data, my_layout = init_plot(stars, labels, repo_links)
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_rep.html')
