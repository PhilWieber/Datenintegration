from SQLManager import SQL

def getFluitId(connection, name:str)-> int:
    query = ''

    query = 'SELECT Id FROM fluessigezutaten WHERE fluessigezutaten.Name = "' + name + '";'
    return SQL.read_query(connection,query)[0][0]


