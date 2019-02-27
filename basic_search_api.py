import requests
import json
from pprint import pprint
DOCKER_SEARCH_URL = "https://store.docker.com/api/content/v1/products/search"
headers = {
    'Search-Version': 'v3'
}
r =  requests.get(DOCKER_SEARCH_URL, headers=headers)
js = r.json()

with open("file.json", "w+") as f:
    json.dump(js['summaries'], f)

