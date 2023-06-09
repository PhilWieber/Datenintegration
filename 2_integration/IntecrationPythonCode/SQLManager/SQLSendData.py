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