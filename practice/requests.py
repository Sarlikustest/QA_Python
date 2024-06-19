import requests

responce = requests.get('https://api.nasa.gov/planetary/apod?api_key=yfG8ixeK2pPidjUqz2cz5q1Yt26bbA7zA7C9LCMK')

data = responce.json()
print(data)