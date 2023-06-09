import mysql.connector
from mysql.connector import Error
import Settings
from JSONManager.SaveLoadJsonDate import loadJsonData
import JSONManager.ListFluits
import JSONManager.LisSupermarkt
import json

from SQLManager import SQL,SQLSendData

if __name__ == '__main__':

   connection = SQL.create_db_connection("localhost", "root", "", "cocktail")
   SQL.deleatAllInformationInDB(connection)

   listAlcoholics = list(JSONManager.ListFluits.getAlcoholicFluits())
   listAlcoholics.sort()
   listNotAlcoholics = list(JSONManager.ListFluits.getNotAlcoholicFluits())
   listNotAlcoholics.sort()

   for alcoholisch in listAlcoholics:
      SQLSendData.sendFluessigezutaten(connection, listAlcoholics.index(alcoholisch), alcoholisch, True)

   for i in range(len(listNotAlcoholics)):
      SQLSendData.sendFluessigezutaten(connection, len(listAlcoholics)+i, listNotAlcoholics[i], False)


   listSupermarktAlcoholic = JSONManager.LisSupermarkt.getSupermarktListAlcoholic()
   listSupermarktNotAlcoholic = JSONManager.LisSupermarkt.getSupermarktListNotAlcoholic()

   for i in range(len(listSupermarktAlcoholic)):
      temp = json.loads(listSupermarktAlcoholic[i])
      SQLSendData.sendSupermarktprodukt(connection,i,temp["name"],float(temp["menge"]),float(temp["preis"]),temp["supermarkt"])

   for i in range(len(listSupermarktNotAlcoholic)):
      temp = json.loads(listSupermarktNotAlcoholic[i])
      SQLSendData.sendSupermarktprodukt(connection,len(listSupermarktAlcoholic)+i,temp["name"],float(temp["menge"]),float(temp["preis"]),temp["supermarkt"])

   for i in range(len(listSupermarktAlcoholic)):
      suchbegriff = json.loads(listSupermarktAlcoholic[i])["suchbegriff"]
      indexDrinks = listAlcoholics.index(suchbegriff)
      SQLSendData.sendFleussigkeitinsupermarkt(connection,i,indexDrinks)

   for i in range(len(listSupermarktNotAlcoholic)):
      try:
         suchbegriff = json.loads(listSupermarktNotAlcoholic[i])["suchbegriff"]
         indexDrinks = listNotAlcoholics.index(suchbegriff)
         SQLSendData.sendFleussigkeitinsupermarkt(connection,len(listSupermarktAlcoholic)+i, indexDrinks+len(listAlcoholics))
      except Exception:
         pass


   print(JSONManager.LisSupermarkt.getSupermarktListAlcoholic())
   #print(loadJsonData(Settings.linkCocktailsJSON))
   create_teacher_table = """
   INSERT INTO fluessigezutaten VALUES
   (1,  'James', true, NULL),
   (2, 'Stefanie',  true,  NULL); 
   """

   connection = SQL.create_db_connection("localhost","root","","cocktail")
   #SQL.execute_query(connection, create_teacher_table)

   #SQL.deleatAllInformationInDB(connection)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
