import json
import Settings


def nameCleaner(input:str):
    temp = input
    temp = temp.replace('\\u00fc',"ü").replace('\\u00dc',"Ü").replace('\\u00df',"ß").replace('\\u00d6',"Ö")\
        .replace('\\u00f6',"ö").replace('\\u00e4',"ä").replace('\\u00c4',"Ä").replace('\\u00a0'," ")
    return(temp)

def mengeCleaner(input:str):
    input.replace(" ","")
    if (" l") in input:
        input = float(input.replace("l",""))

    else:
        input = input.replace("ml","")
        input = input.replace("g", "")
        input = float(input)/1000
    return input


def getSupermarktListAlcoholic():
    urlJson = Settings.linkSupermarkAlcoholicJSON
    data = open(urlJson, encoding='utf-8').read()
    jsonData = json.loads(data)
    jData = jsonData["fluits"]
    output = list()
    for data in jData:
        dataTemp = json.loads(data)
        sbegriff = nameCleaner(dataTemp["suchbegriff"])
        name= nameCleaner(dataTemp["name"])
        handelsmarkr = nameCleaner(dataTemp["handelsmarke"])
        preis = dataTemp["preis"]
        menge = mengeCleaner(dataTemp["menge"])
        supermarkt = nameCleaner(dataTemp["supermarkt"])
        temp = json.dumps({"suchbegriff": sbegriff, "name": name, "handelsmarke":  handelsmarkr, "preis": preis, "menge": menge, "supermarkt": supermarkt})
        output.append(temp)
    return(output)

def getSupermarktListNotAlcoholic():
    urlJson = Settings.linkSupermarkNotAlcoholicJSON
    data = open(urlJson, encoding='utf-8').read()
    jsonData = json.loads(data)
    jData = jsonData["fluits"]
    output = list()
    for data in jData:
        dataTemp = json.loads(data)
        if "g" in dataTemp["menge"]:
            continue
        sbegriff = nameCleaner(dataTemp["suchbegriff"])
        name= nameCleaner(dataTemp["name"])
        handelsmarkr = nameCleaner(dataTemp["handelsmarke"])
        preis = dataTemp["preis"]
        menge = mengeCleaner(dataTemp["menge"])
        supermarkt = nameCleaner(dataTemp["supermarkt"])
        temp = json.dumps({"suchbegriff": sbegriff, "name": name, "handelsmarke":  handelsmarkr, "preis": preis, "menge": menge, "supermarkt": supermarkt})
        output.append(temp)
    return(output)