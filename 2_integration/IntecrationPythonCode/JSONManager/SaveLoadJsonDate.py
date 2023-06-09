import json

def saveJsonData(link, jsonData):
    with open(link, 'w') as outfile:
        outfile.write(jsonData)

def loadJsonData(link):
    with open(link) as user_file:
        parsed_json = json.load(user_file)
    return parsed_json