import json
import Settings

def getRezepts():
    urlJson = Settings.linkCocktailsJSON
    data = open(urlJson,  encoding='utf-8').read()
    jsonData = json.loads(data)
    jData = jsonData["drinks"]

    return jData