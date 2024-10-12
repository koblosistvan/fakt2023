# ------ XML2JSON_FILTER ------
# fájlkezelőben megnyitva van prompt,
# alternatívan az xml_filter_SETTINGS.txt használható beállításhoz

# ========================================================================================
napok = [True, False, True, False, True] # True filterez, False nem (hetfotol pentekig)
# kedden meg csutortokon lesz nyilt nap, ez alapjan van beallitva
# ========================================================================================
CONST_NAPOK = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "? (y/n): "]
CONST_VALIDATE = [("y","n","igen","nem"), ("y","igen")]
EXPORT_AS_DATA_VAR = True
GUI_PROMPT = False # deprekált konzol interface
# az exportált fájl egy js, amiben egy 'data' nevű array van, abban minden elem json object
# mivel a js nem nyithat meg fájlokat, ezért egy html dokumentum head tagjébe kell belinkelni egy 'link' taggel


import json
def panic():
    input("Nyomj entert a bezáráshoz")
    print("-"*40)
    quit()

def vonal():
    print("-"*30)
vonal()
print("log:")

# lokálisan kell lennie ugyanabban a mappában
# az "xml2json.py" készíti el, alapértelmezett nevén "orarend_export.json"
#filename = "nyiltnapp0531\\xml2json\\orarend_export.json"
filename = "orarend_export.json"

try:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.loads(f.read())
except:
    print("HIBA TÖRTÉNT A FÁJL MEGNYITÁSAKOR")
    panic()

# console filter settings

while (GUI_PROMPT):
    for i in range(5):
        while True:
            prompt = input(f"{CONST_NAPOK[i]} {CONST_NAPOK[-1]}").strip().lower()
            if prompt in CONST_VALIDATE[0]:
                break
        if prompt in CONST_VALIDATE[1]:
            napok[i] = True
        else:
            napok[i] = False
    print("-"*10)
    print("Ezek a napok lesznek törölve:")
    print("-"+", -".join([CONST_NAPOK[i] for i in range(5) if (napok[i])]))

    prompt = input("Folytatás? (ENTER): ").strip().lower()
    if prompt=="":
        break

# szűrés beállítása

hetfo = napok[0]
kedd = napok[1]
szerda = napok[2]
csutortok = napok[3]
pentek = napok[4]

# szűrés
l = len(data)
noneCounter = 0   # a filterezendo elemeket none-re irja at, vegen ki lesznek torolve

for i in range(len(data)):
    if napok[int(data[i]["day"])]:
        data[i] = None
        noneCounter += 1

vonal()

# cleanup
for _ in range(data.count(None)):
    data.remove(None)


print(f"{l - len(data)}/{l} elem került filterezésre.")

# ugyanaz a kod ami az xml2jsonban van
export = json.dumps(data, ensure_ascii=False, indent=4).encode('utf8')
#    exportFileName = 'nyiltnapp0531\\xml2json\\orarend-export-filterezett.js'
exportFileName = 'orarend-export-filterezett.js'
if not EXPORT_AS_DATA_VAR:
    exportFileName += 'on'
with open(exportFileName, 'w', encoding='utf-8') as f:
    if EXPORT_AS_DATA_VAR:
        f.write('data = ')
    f.write(export.decode())
    print("Szűrt JSON fájl sikeresen létrehozva.")

sqlFileName = 'orarend.sql'
with open(sqlFileName, 'w', encoding='utf-8') as f:
    sql_stmt = "TRUNCATE TABLE `lessons`;"
    print(sql_stmt, file=f)
    sql_stmt = "INSERT INTO `lessons` (`id`, `room`, `period`, `start_time`, `end_time`, `subject`, `teacher`, `day`, `class`, `grade`, `student_group`, `level`, `language`, `valid`, `last_upd`) VALUES "
    print(sql_stmt, file=f)
    for i in range(len(data)):
        row = data[i]
        sql_stmt = f" ({row['id']}, '{row['room']}', {row['period']}, '{row['starttime']}', '{row['endtime']}', '{row['subject']}', '{row['teacher']}', '{row['day']}', '{row['class']}', {row['grade'] if len(row['grade']) > 0 else 'null'}, '{row['studentgroup']}', '{row['level']}', '{row['language']}', 1, now())"
        if i < len(data)-1:
            sql_stmt += ', '
        else:
            sql_stmt += ';'
        print(sql_stmt, file=f)
    sql_stmt = "UPDATE `lessons` set `language` = null WHERE `language` = 'None';"
    print(sql_stmt, file=f)
    sql_stmt = "UPDATE `lessons` set `grade` = null WHERE `grade` = 0;"
    print(sql_stmt, file=f)

    print("Szűrt SQL fájl sikeresen létrehozva.")

vonal()
