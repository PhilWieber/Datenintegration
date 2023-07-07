import json
import Settings

def is_number(input:str)->bool:
    input = input.replace(",",".")
    input = input.replace("/", ".")
    try:
        float(input)
    except:
        return False
    return True

def removeVolume(input:str):
    input = input.split(" ")
    output = ""
    if is_number(input[0]):
        input = input[2:]
    for i in range(len(input)):
        output += " "+ input[i]
    return output[1:]

def setAlcoholicIngredients(urlJsonData:str):
    data = open(urlJsonData,  encoding='utf-8').read()
    jsonData = json.loads(data)
    jData = jsonData["drinks"]


    alkoholischeZutaten = set()
    for i in jData:
        daten: dict = i["Daten"]
        if 'Zutaten (alkoholisch)' in daten.keys():
            for i in daten['Zutaten (alkoholisch)']:
                alkoholischeZutaten.add(removeVolume(i))

    return alkoholischeZutaten


def setNotAlcoholicIngredients(urlJsonData:str):
    data = open(urlJsonData,  encoding='utf-8').read()
    jsonData = json.loads(data)
    print(type(jsonData))
    jData = jsonData["drinks"]

    alkoholfreieZutaten = set()
    for i in jData:
        daten:dict = i["Daten"]
        if 'Zutaten (nicht alkoholisch)' in daten.keys():
            for i in daten['Zutaten (nicht alkoholisch)']:
                alkoholfreieZutaten.add(removeVolume(i))

    return alkoholfreieZutaten


def cleanAlcoholicSet(input:set):
    output = set()
    for i in input:
        temp = str(i).replace("Whisk(e)y","Whisky").replace("Whiskey","Whisky")\
            .replace("Ora-Likör - Lochan","Ora Likör Lochan").replace("Lochan Ora","Ora Likör Lochan").replace("Wodka-Orange","Wodka Orange").replace("1","").replace("2","").replace("etwas","").replace("auffüllen","")
        output.add(temp)
    return output

def cleanNotAlcoholicSet(input:set):
    output = set()
    for i in input:
        temp = str(i).replace("(Saft)","Saft").replace("(Sirup)","Sirup")\
            .replace("(saft)","Saft").replace("(Limo)","Limo").replace("(Sauce)","Saft").replace("Juice","Saft").replace("- Granini", "Saft")\
            .replace("Anapam - Becker´s Bester","Ananassaft").replace("- Becker´s Bester", "Saft").replace("(Konze)", "Konzentrat").replace("- Ocean Spray", "Saft")\
            .replace(" - Giffard","-Giffard").replace(" - Riemerschmid","-Riemerschmid").replace(" - Klindworth","-Klindworth")\
            .replace(" - Jamaica","-Jamaica").replace(" - Bardinet","-Bardinet").replace(" - Roses","-Roses").replace(" - Marie","-Marie")\
            .replace(" - Monin","-Monin").replace(" - Monin","-Monin").replace("1-1/2 ","").replace("1-2 ","").replace("12","").replace("1Tasse ","")\
            .replace("7 or 5 ","").replace("4","").replace("3","").replace("2","").replace("1","").replace("o,75 Lit. alkoholfreier Sekt","alkoholfreier Sekt")\
            .replace("Öl Saft","Öl").replace("etwas ","").replace("beliebige ","").replace("etwas ","").replace("auffüllen ","")
        output.add(temp)
    return output

def containsWantedElement(input:str, listWantedElement:list)->bool:
    for i in listWantedElement:
        if(str(i).lower() in input.lower()):
            return True
    return False

def sortOutUnwantedNotAlcoholicSubstance(input:set):
    wanted = ["limo", "Sprite", "Mountain Dew", "Hot Buttered Rum", "Pastis", "alkoholfrei", "Water", "Sanbitter",
              "Monin", "Marie", "Roses", "Monin", "Fragola Boero", "Frothee", "Vermouth Rosso", "Tom Collins-Mix",
              "Ocean Spray Cr.", "Bardinet", "Necta", "Klindworth", "Jamaica", "Riemerschmid", "Giffard",
              "San Pellegrino", "Vermouth Bianco", "Ginger Ale", "Molke", "Cranberry Blackcurrant", "Sangrita", "Pulco",
              "brühe", "Seven up", "Sangria", "Negrita", "Säfte", "wasser", "nektar", "San ", "Essig", "Red Bull",
              "Likör", "Apollinari", "Konzentrat", "Kakao", "Espresso", "Cola", "saft", "Bitter Lemon", "Rivella",
              "Sirup", "Fanta", "Tee", "Trink", "Schweppes", "Kaffee", "Kakao", "Suppe", "milch", "Öl", "konzentrat",
              "auffüllen", "Sekt","Mattoni Peach","Kombucha","Robby bubble","T V Mai Tai Mix","Rabarbaro Zucca","Falernum",
              "T.V.Navy Grog"]
    unwanted = ["Püree", "mehl", "schale", "beer", "salat","Lindavia B-Vit", "Trauben", "Butter", "Cocktail", "Rohmarzipan", "Apotheke",
                "Kerbel", "Ananas", "Gelee", "Obst", "Zimt", "Thymian", "Knoblauch", "Schattenmorellen", "mus",
                "Dextro", "Mayonnaise", "Ingwer", "ganz", "blüte", "Beeren", "geputzt", "Blatt", "Crème Fraiche",
                "zerklein", "Ovomaltine", "Mandel", "Koriander", "eingelegt", "Gelatine", "Safran", "geviertel",
                "flocken", "halbiert", "Petersilie", "Masse", "Basilikum", "Sorbet", "Spargel", "Kräuter", "hälft",
                "Haferflocken", "kugeln", "Schokolade", "Bete", "Kohlrabi", "Radieschen", "kandiert", "Feige",
                "Marmelade", "geviertelt", "getrocknet", "wurzel", "peeld", "Crushed", "Ice", "Muskatnuß", "groß",
                "Datteln", "ungeschält", "Kümmel", "fond", "Kresse", "Eigelb", "konfit", "blätter", "Dose", "Quark",
                "geachtelt", "splitter", "zerstoßene", "Block", "fein", "klein", "pürier", "Rosen", "Rosinen",
                "Sternanis", "Eis", "Dry", "zweig", "Glas", "gemahlen", "Ei(er)", "Rohmasse", "Meerrettich", "Avokado",
                "schote", "kern", "spalte", "aroma", "gurke", "knolle", "schale", "ketchup", "raspel", "Spinat",
                "würfel", "mark", "Glas", "geschält", "gefroren", "pürierte", "paste", "Sahne", "Früchte", "Kirsche",
                "Mango", "creme", "Würfeln", "stange", "Gewürz", "Bohne", "Süßstoff", "natur", "Zehe", "Honig",
                "Schnitt", "zerdrückte", "Paprika", "frischkäse", "zucker", "Sellerie", "Rhabarber", "pürre", "keime",
                "Stengel", "Joghurt", "Pfeffer", "salz", "Dose", "pulver", "eis", "gehackt", "frisch", "gerieben",
                "gerforen", "hefe", "Zwiebel", "Dill", "Fresh", "geraspelt", "Cream", "Stangen", "Scheibe", "körn",
                "Stück", "Marmalade", "geraschpelt", "Frucht", "gemahlenen", "dünn", "Reif","Carpe Diem Kefir"]

    outputSetWanted = set()
    outputSetUnwanted = set()
    outputSetUnshure = set()

    for subject in input:
        if(containsWantedElement(subject,wanted)):
            outputSetWanted.add(subject)
        elif(containsWantedElement(subject,unwanted)):
            outputSetUnwanted.add(subject)
        else:
            outputSetUnshure.add(subject)

    return[outputSetWanted,outputSetUnwanted,outputSetUnshure]


def simplifySet(input:set):
    output = set()
    for i in input:
        temp = i
        if "(" in temp:
            temp = temp[:temp.find("(")]
        if " - " in temp:
            temp = temp[:temp.find(" - ")]
        output.add(temp)
    return output

def setEndclean(input:set):
    output = set()
    for i in input:
        temp = str(i)
        while len(temp)> 1 and temp[0]== " ":
            temp = temp[1:]
        while len(temp)> 1 and temp[-1]== " ":
            temp = temp[:-1]
        if "cl " in temp:
            temp = temp.replace("cl ", "")
        output.add(temp)
    output.remove("")
    return output




def getAlcoholicFluits()->list:


    urlJson= Settings.linkCocktailsJSON

    alkoholischeZutaten = setAlcoholicIngredients(urlJson)
    print(len(alkoholischeZutaten))
    alkoholischeZutaten = cleanAlcoholicSet(alkoholischeZutaten)
    print(len(alkoholischeZutaten))
    alkoholischeZutaten = simplifySet(alkoholischeZutaten)
    print(len(alkoholischeZutaten))
    alkoholischeZutaten = setEndclean(alkoholischeZutaten)
    return(alkoholischeZutaten)


def getNotAlcoholicFluits():
    urlJson = Settings.linkCocktailsJSON
    alkoholfreieZutaten = setNotAlcoholicIngredients(urlJson)
    alkoholfreieZutaten = cleanNotAlcoholicSet(alkoholfreieZutaten)
    alkoholfreieZutaten = sortOutUnwantedNotAlcoholicSubstance(alkoholfreieZutaten)[0]
    alkoholfreieZutaten = simplifySet(alkoholfreieZutaten)
    alkoholfreieZutaten = setEndclean(alkoholfreieZutaten)
    print(alkoholfreieZutaten)
    return (alkoholfreieZutaten)