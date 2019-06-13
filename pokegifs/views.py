from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
import json
import requests
import os
from random import randint

def pokemon_details(request, id):
    # USING PokeAPI
    api_url = f"http://pokeapi.co/api/v2/pokemon/{id}/"
    res = requests.get(api_url)
    if res.status_code == 404:
        return HttpResponseNotFound("<h1>Gotta catch 'em all!</h1>" + "\n" + "<h3>..except this one.</h3>" + "Pokemon Not found. Please try again") 

    body = json.loads(res.content)
    name = body["name"]
    pokemon_id = body["id"]
    pokemon_type = body["types"]

    # USING GIPHY API
    key = os.environ.get("GIPHY_KEY")
    url = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={name}&rating=g"
    res = requests.get(url)
    body = json.loads(res.content)
    if res.status_code == 403:
        return HttpResponseNotFound("<h1>STOP RIGHT NOW!</h1>" + "\n" + "<h3>Thank you very much.</h3>" + "Your key is invalid. I told you not to trust.")

    data = body["data"]
    index = randint(0,len(data)-1)
    gif_url = data[index]['url']

    context = {
        "name": name,
        "id": pokemon_id,
        "type":[],
        "gif": gif_url
        }
    for t in pokemon_type:
        context["type"].append(t["type"]["name"])

    return JsonResponse(context)



