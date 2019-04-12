import json
import boto3
import botocore.vendored.requests as requests
import datetime
s3 = boto3.resource('s3')
BUCKET_NAME = 'docker-recent'


def lambda_handler(event, context):
    data = download_data()
    obj = s3.Object(BUCKET_NAME, "recent_" + datetime.utcnow().strftime("%d-%m-%h") + ".json")
    obj.put_object(
        Body = json.dumps(data)
    )
    return {
        'statusCode': 200,
        'body': data['count']
    }


SEARCH_URL = "https://store.docker.com/api/content/v1/products/search"
HEADERS = {
    'Search-Version': 'v3'
}

PARAMS = {
    'sort': 'updated_at',
    'order': 'desc',
    'count': 5000
}


def download_data():
    resp = {}
    r = requests.get(SEARCH_URL, headers=HEADERS, params=PARAMS)
    resp_data = r.json()
    resp['count'] = resp_data['count']
    resp['summaries'] = resp_data['summaries']
    return resp
