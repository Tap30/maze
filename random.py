import os
import requests
import json
from urllib.parse import urljoin

url = os.environ.get('URL', 'http://127.0.0.1:8000')
api_pre = os.environ.get('API', '/')
API = urljoin(url, api_pre)


def parse_response(response):
    if int(response.status_code / 100) != 2:
        print('Unsuccessful status code {}'.format(response.status_code))
        if response.content:
            print(response.content.decode('utf-8'))
    else:
        data = json.loads(response.content.decode('utf-8'))
        print('Successful')
        for key in data:
            print('{}: {}'.format(key, data[key]))
        return data


def hidden(auth):
    address = urljoin(API, '/race/h1dden')
    res = requests.get(address, headers=dict(Authorization='Bearer {}'.format(auth)))
    return parse_response(res)