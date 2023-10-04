adat = open('5a-magasugras2.txt', mode='r', encoding='utf-8')

tavaly = []
idén = []

for i in adat:
    ti = i.split(';')
    tavaly.append(int(ti[0]))
    idén.append(int(ti[1]))
print(f'tavaly a legkisebb ugrás: {min(tavaly)} a legnagyobb: {max(tavaly)}')
print(f'idén a legkisebb ugrás: {min(idén)} a legnagyobb: {max(idén)}')

adat.close()

idei_max_id = 0
idei_max_magassag = idén[0]
ideiminid = 0
ideiminmagassag = idén[0]
tavaly_max_id = 0
tavalymaxmagassag = tavaly[0]
tavalyminid = 0
tavalyminmagassag = tavaly[0]

for i in range(1, len(idén)):
    if idén[i] > idei_max_magassag:
        idei_max_magassag = idén[i]
        idei_max_id = i

for i in range(1, len(idén)):
    if idén[i] < ideiminmagassag:
        ideiminmagassag = idén[i]
        ideiminid = i

for i in range(1, len(tavaly)):
    if tavaly[i] > tavalymaxmagassag:
        tavalymaxmagassag = tavaly[i]
        tavaly_max_id = i

for i in range(1, len(tavaly)):
    if tavaly[i] < tavalyminmagassag:
        tavalyminmagassag = tavaly[i]
        tavalyminid = i
print(f'A legnagyobb ugrás: {idei_max_magassag} és {idei_max_id} ugrotta')
print(f'A legkisebb ugrás: {ideiminmagassag} és {ideiminid} ugrotta')
print(f'A legnagyobb ugrás: {tavalymaxmagassag} és {tavaly_max_id} ugrotta')
print(f'A legkisebb ugrás: {tavalyminmagassag} és {tavalyminid} ugrotta')
#
