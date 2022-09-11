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


def login(phone):
	address = urljoin(API, '/programmer/login')
	res = requests.post(address, json=dict(phone=phone))


def verify(phone, code):
	address = urljoin(API, '/programmer/verify')
	res = requests.post(address, json=dict(phone=phone, code=code))
	return parse_response(res)