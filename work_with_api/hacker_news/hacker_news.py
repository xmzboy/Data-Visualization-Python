import json
import requests

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

r = requests.get(url)

response_dict = r.json()

with open('data/readable_hn_data.json', 'w') as f:
    json.dump(response_dict, f, indent=4)