import requests
import json

DOCKER_SEARCH_URL = "https://store.docker.com/api/content/v1/products/search"
HEADERS = {
    'Search-Version': 'v3'
}


def get_basic_data():
    # Get basic info:
    r = requests.get(DOCKER_SEARCH_URL, headers=HEADERS, params={'page_size': 1000})
    skeleton_data = r.json()
    data = {}
    data['count'] = skeleton_data['count']
    data['summaries'] = skeleton_data['summaries']

    for i in range(100):
        print(i)
        next_url = skeleton_data['next']
        print(next_url)
        with requests.get(next_url, headers=HEADERS, params={'page_size': 1000}) as r2:
            skeleton_data = r2.json()
            with open('search_data.json', 'w+') as f2:
                j = data
                # print(j)
                print(len(j['summaries']))
                j['summaries'].extend(skeleton_data['summaries'])
                json.dump(j, f2, indent=1)
        # with open('search_data.json', 'r+') as f2:
        #     # print(len(f2.readlines()))
        #     j = json.load(f2)
        #     print(len(j['summaries']))
        print()


if __name__ == '__main__':
    get_basic_data()
