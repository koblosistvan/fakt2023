# ------ XML2JSON ------

EXPORT_AS_JAVASCRIPT = False  # kiterjesztés beállítása:
# false => .json , true => .js

EXPORT_SQL_TXT = True # csinal egy txt fajlt benne insert into parancsokkal

USE_DEFAULT_FILENAME = True


# index szerint sorban vannak, az ARGS eleme lesz átalakítva a TABLE azonos indexű elemévé
CONST_RENAME_ARGS = ["Biológia - egészségtan", # újranevezendo tantargyak
                     "Informatika",
                     "Egyházi Ének",
                     "Ének-zene",
                     "Technika és tervezés",
                     "Testnevelés és sport",
                     "Történelem, társadalmi és állampolgári ismeretek"]
CONST_RENAME_TABLE = ["Biológia", # rendre ezekre nevezi at
                      "Digitális Kultúra",
                      "Ének",
                      "Ének",
                      "Technika",
                      "Technika",
                      "Testnevelés",
                      "Testnevelés"]

def renameSubject(sub):
    if (sub in CONST_RENAME_ARGS): # ha újranevezendő tantárgy
        return CONST_RENAME_TABLE[ CONST_RENAME_ARGS.index(sub) ] # return átnevezett
    return sub

def vonal():
    print("-"*40)
vonal()

def count_tobb(txt, *args): # tesztelés illegális fájlnév karakterekre
    for i in range(len(args)):
        if txt.count(args[i]):
            return True
    else:
        return False

def testForLevel(group): # true: "emelt szint"; false: "alap szint"
    group = group.lower()
    if bool(group.count("alap")):
        group = False
    elif bool(group.count("emelt")):
        group = True
    elif bool(group.count("e/")):
        group = True
    elif bool(group.count(" e/")):
        group = True
    else:
        group = False
    if group:
        return "emelt"
    else:
        return "alap"

def testForNyelv(group): # true, ha angol/német/orosz/francia, kulonben false
    group = group.lower()
    if bool(group.count("angol")) or bool(group.count("német")):
        return True
    elif bool(group.count("francia")) or bool(group.count("orosz")):
        return True
    else:
        return False
def findNyelvLevel(group):
    group = group.lower()
    if bool(group.count("francia")) or bool(group.count("orosz")):
        return "masodik"
    elif bool(group.count("angol 2")) or bool(group.count("német 2")):
        return "masodik"
    else:
        return "elso"

# BEÁLLÍTÁSOK
doUnicodeCheck = True  # ellenőrzi, hogy az xml dokumentum karakterkódolása UTF-8
doHanyadikNyelv = True # első, vagy második a tanult nyelv (!! NEM MŰKÖDIK !!)
doShortNames = False # a tanárok neveinek rövidítéseit is kigyűjti (FELESLEGES)
doFullRooms = False # a termek teljes neveit is kigyűjti (FELESLEGES)
# - - - - - - - - - - - -

from bs4 import BeautifulSoup
import json


<<<<<<< HEAD
filename = 'nyiltnapp0531\\xml2json\\orarend_2022_23_2.xml'
filename = 'orarend_2022_23_2.xml'
=======
#filename = 'nyiltnapp0531\\xml2json\\orarend_2024_25_2008_.xml'
filename = 'orarend_2024_25_2008_.xml' # PyCharm formátum
>>>>>>> 3356838d96954cc1eae1aaf1139b14bfe676e933

if not(USE_DEFAULT_FILENAME):
    try:
        prompt = input("Fájlnév: ").strip().split('.')[0]
        if (prompt=="") or count_tobb(prompt,'.',';',':','/','\\','*','(',')','{','}','<','>','[',']','='):
            raise Exception
        else:
            filename = prompt + ".xml"
    except:
        print("Hibás fájlnév")
        quit()

#print(soup.prettify())

if doUnicodeCheck:
    print("Karakterkódolás ellenőrzése...")
    try:
        with open(filename,'r', encoding="utf-8") as check:
            if check.readline().count("utf-8") == 0:
                print("A fájl karakterkódolása nem megfelelő, a szövegek olvashatatlanak lehetnek.")
                if input("Kívánja folytatni? (y/n)") in ("y","Y"):
                    pass
                else:
                    print("END")
                    quit()
    except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError):
        print("KARAKTERKÓDOLÁSI HIBA")
        quit()
    except (FileNotFoundError):
        print("A FÁJL NEM TALÁLHATÓ")
        quit()
    except:
        print("ISMERETLEN HIBA TÖRTÉNT")
        quit()
    else:
        pass
else:
    print("FIGYELMEZTETÉS: A karakterkódolás ellenőrzése ki van kapcsolva.")


with open(filename,'r', encoding="utf-8") as f:  #encoding dolog
    content = f.read()
    xample = BeautifulSoup(content, 'xml')

cards = xample.find_all('card')
#teachers = xample.find_all('teacher')
#subjects = xample.find_all('subject')
#classrooms = xample.find_all('classroom')
#classes = xample.find_all('class')
#groups = xample.find_all('group')
#periods = xample.find_all('period')


l = len(cards)
kinyert = [{} for _ in range(l)]

#print(xample.find_all("lesson", {"id": "*8"}))

print("Előkészületek...")
for i in range(l):
    kinyert[i]["lessonid"] = cards[i]["lessonid"]

print("Osztálytermek...")
for i in range(l):
    temp = cards[i]
    if temp["classroomids"]:
        kinyert[i]["room"] = xample.find("classroom", {"id": temp["classroomids"]})["short"]
        kinyert[i]["roomFull"] = xample.find("classroom", {"id": cards[i]["classroomids"]})["name"]
    else:
        kinyert[i]["room"] = ''
        kinyert[i]["roomFull"] = ''


print("Óraszámok...")
for i in range(l):
    kinyert[i]["period"] = cards[i]["period"]

print("Időpontok...")
for i in range(l):
    temp = cards[i]
    kinyert[i]["starttime"] = xample.find("period", {"period": temp["period"]})["starttime"]
    kinyert[i]["endtime"] = xample.find("period", {"period": temp["period"]})["endtime"] #lehet kesobb optimailzalni ugy hogy +45

print("Tanárok...")
for i in kinyert:
    temp = i["lessonid"]
    i["teacherid"] = xample.find("lesson", {"id": temp})["teacherids"]
    i["subject"] = xample.find("lesson", {"id": temp})["subjectid"]

print("Tanárok nevei...")
for i in kinyert:
    temp = i["teacherid"]
    i["teacher"] = xample.find("teacher", {"id": temp})["name"]

if doShortNames:
    for i in kinyert:
        temp = i["teacherid"]
        i["teacherShort"] = xample.find("teacher", {"id": temp})["short"]


print("Tantárgyak...")
for i in kinyert:
    temp = i["subject"]
    i["subject"] = xample.find("subject", {"id": temp})["name"]
    i["subject"] = renameSubject( i["subject"] ) # rossz nevűeket egységesíti

print("Napok...")
for i in range(l):
    temp = cards[i]["day"]
    kinyert[i]["day"] = xample.find("day", {"day": temp})["day"]

print("Osztályok...")
for i in kinyert:
    temp = i["lessonid"]
    i["class"] = xample.find("lesson", {"id": temp})["classids"]
    if bool(i["class"].count(",")):
        i["class"] = i["class"].split(",")
        for j in range(len(i["class"])):
            i["class"][j] = xample.find("class", {"id": i["class"][j]})["name"]
        i["class"] = ','.join(sorted(i["class"])).replace('*','')
    elif i["class"]:
        i["class"] = xample.find("class", {"id": i["class"]})["name"]
        
print("Évfolyamok...")
for i in kinyert:
    if isinstance(i["class"], list):
        i["grade"] = i["class"][0].split(".")[0]
    else:
        i["grade"] = i["class"].split(".")[0]

print("Csoportok szintjei...")
if doHanyadikNyelv:
    print("Első/második nyelv...")

for i in kinyert:
    temp = i["lessonid"]
    i["level"] = ''
    i["language"] = None
    i["studentgroup"] = xample.find("lesson", {"id": temp})["groupids"]
    if bool(i["studentgroup"].count(",")):
        i["studentgroup"] = i["studentgroup"].split(",")
        for j in range(len(i["studentgroup"])):
            i["studentgroup"][j] = xample.find("group", {"id": i["studentgroup"][j]})["name"]
        i["studentgroup"] = 'Több csoport'

        tempindex = i["studentgroup"][0]
        i["level"] = testForLevel(tempindex)

        if not doHanyadikNyelv: # skip mert ez egy work in progress feature
            continue

        if testForNyelv(tempindex):
            i["language"] = findNyelvLevel(tempindex)
        else:
            i["language"] = None

    elif i["studentgroup"]:
        i["studentgroup"] = xample.find("group", {"id": i["studentgroup"]})["name"]
        i["level"] = testForLevel(i["studentgroup"])

        if not doHanyadikNyelv:
            continue

        tempindex = i["studentgroup"]
        if testForNyelv(tempindex):
            i["language"] = findNyelvLevel(tempindex)
        else:
            i["language"] = None


        
# felesleg törlése
print("Rendrakás...")
for i in kinyert:
    del i["lessonid"]
    del i["teacherid"]

if not doFullRooms:
    for i in kinyert:
        del i["roomFull"]

for i in kinyert:
    temp = i["group"]
    if isinstance(temp, list) and len(set(temp))==1:
        i["group"] = i["group"][0]

print("Azonosítók...")
for i in range(len(kinyert)):
    kinyert[i]["id"] = i


print("JSON fájl enkódolása...")
export = json.dumps(kinyert, ensure_ascii=False, indent=4).encode('utf8')

# NINCS TRYCATCH
<<<<<<< HEAD
exportFileName = 'nyiltnapp0531\\xml2json\\orarend_export.json'
exportFileName = 'orarend_export.json'

=======
#exportFileName = 'nyiltnapp0531\\xml2json\\orarend_export.json'
exportFileName = 'orarend_export.json'
>>>>>>> 3356838d96954cc1eae1aaf1139b14bfe676e933
if EXPORT_AS_JAVASCRIPT:
    exportFileName = 'orarend_export.js'

with open(exportFileName,'w',encoding='utf-8') as f:
    f.write(export.decode())
    print("JSON fájl sikeresen exportálva.")

if EXPORT_SQL_TXT:
    print("SQL text fájl elkészítése...")
    with open("sql_insert_into.txt",'w',encoding="utf-8") as q:
        for i in range(len(kinyert)):
            temp = "INSERT INTO lessons VALUES ("

            temp += "'" + str(kinyert[i]["id"]) + "', "
            temp += "'" + kinyert[i]["room"] + "', "
            temp += "'" + str(kinyert[i]["period"]) + "', "
            temp += "'" + kinyert[i]["starttime"] + "', "
            temp += "'" + kinyert[i]["endtime"] + "', "
            temp += "'" + kinyert[i]["subject"] + "', "
            temp += "'" + kinyert[i]["teacher"] + "', "
            temp += "'" + kinyert[i]["day"] + "', "

            if isinstance(kinyert[i]["class"], list):
                temp += "'" + ", ".join(kinyert[i]["class"]) + "', "
            else:
                temp += "'" + kinyert[i]["class"] + "', "

            temp += "'" + kinyert[i]["grade"] + "', "

            if isinstance(kinyert[i]["group"],list):
                temp += "'" + ", ".join(kinyert[i]["group"]) + "', "
            else:
                temp += "'" + kinyert[i]["class"] + "', "

            temp += "'" + kinyert[i]["level"] + "', "
            if kinyert[i]["hanyadikNyelv"]==None:
                temp += "NULL"
            else:
                temp += "'" + kinyert[i]["hanyadikNyelv"] + "'"

            temp += ");\n"
            q.write(temp)

print("END")



#print(len(xample.find_all('card')))
#print(len(xample.find_all('lesson')))


vonal()

