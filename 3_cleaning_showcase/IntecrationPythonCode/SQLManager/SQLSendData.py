from SQLManager import SQL

def sendFluessigezutaten(connection, id:int, name:str, alkoholisch:bool, farbe:str=None):
    query = ''
    if farbe == None:
        query ='INSERT INTO fluessigezutaten VALUES ('+ str(id) + ', "'+ name +'", '+str(alkoholisch).lower() +', NULL);'
    else:
        query = 'INSERT INTO fluessigezutaten VALUES (' + str(id) + ', "' + name + '", ' + str(alkoholisch).lower() + ', "'+farbe+');'

    SQL.execute_query(connection,query)


def sendFleussigkeitinsupermarkt(connection,supermarktproduktId:int,fluessigkeitId:int):
    query = 'INSERT INTO fleussigkeitinsupermarkt VALUES (' + str(supermarktproduktId) + ', ' + str(fluessigkeitId) +  ');'

    SQL.execute_query(connection, query)

def sendSupermarktprodukt(connection, id:int, name:str, produktmenge:int, preis:int, supermarkt:str):
    query = 'INSERT INTO supermarktprodukt VALUES (' + str(id) + ', "' + str(name) + '", ' + str(produktmenge) +', ' + str(preis) +', "' + str(supermarkt) +  '");'
    SQL.execute_query(connection, query)

def sendRezeptGrunddaten(connection, id: int, name: str, kategorie: str, jahreszeit: str, Glas: str):
    query = 'INSERT INTO rezept VALUES (' + str(id) + ', "' + str(name) + '", "' + str(
        kategorie) + '", "' + str(jahreszeit) + '", "' + str(Glas) + '",NULL,NULL);'
    SQL.execute_query(connection, query)


def sendRezept(connection,jsonRezept:list):
    for i in range(len(jsonRezept)):
        rezept= jsonRezept[i]
        id = i
        name: str = rezept["Name"]
        daten = rezept["Daten"]
        kategorie: str =daten["Allgemeine Informationen"]["Kategorie"]
        jahreszeit: str =daten["Allgemeine Informationen"]["Jahreszeit"]
        glas: str = daten["Zubereitung"]["Glas"]
        sendRezeptGrunddaten(connection,id,name,kategorie,jahreszeit,glas)