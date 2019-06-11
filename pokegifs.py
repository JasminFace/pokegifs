import json
import requests
import os


res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)

name = body["name"]
id = body["id"]
type = body["types"]


key = os.environ.get("GIPHY_KEY")
url = "https://api.giphy.com/v1/gifs/search?api_key={}&q=pikachu&rating=g".format(key)
res = requests.get(url)

body = json.loads(res.content)
data = body["data"]
pika_19 = data[19]['url']

print(pika_19)
