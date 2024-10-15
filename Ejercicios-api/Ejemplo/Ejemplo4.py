#coding: latin1
from urllib import response
from pip._vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"

response = requests.get(api_url)
print(response.json())

cambio = {'title': '4K'}

response = requests.patch(api_url, json = cambio)
print(response.json())
print(response.status_code) 