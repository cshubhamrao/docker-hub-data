import requests

url = "https://hub.docker.com/api/content/v1/products/search"

querystring = {"page_size": "25", "q": "", "type": "image", "page": "3"}

payload = ""
headers = {
    'cache-control': "no-cache",

}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)

'''For repositories'''

# url = "https://hub.docker.com/v2/repositories/library/busybox/"

# payload = ""
# headers = {
#     'cache-control': "no-cache",
# }

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# print(response.text)

'''For DockerFiles (available across a few repos only)'''
# url = "https://hub.docker.com/v2/repositories/swce/keyval-resource/dockerfile/"

# payload = ""
# headers = {
#     'cache-control': "no-cache",
# }

# response = requests.request("GET", url, data=payload, headers=headers)

# print(response.text)
