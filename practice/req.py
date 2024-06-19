import requests

responce = requests.get('https://api.github.com/events')
data = responce.json()
print(data)