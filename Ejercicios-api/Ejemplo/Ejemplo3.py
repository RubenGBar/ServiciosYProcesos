#coding: latin1
from urllib import response
from pip._vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)
print(response.json())

cambio = {'userId': 1, 'id': 10, 'title': 'Wash Car', 'completed': True}

response = requests.put(api_url, json = cambio)
print(response.json())
print(response.status_code)