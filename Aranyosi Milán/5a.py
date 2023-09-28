forras = open('5a-magasugras2.txt', mode='r', encoding='utf-8')

tavaly = []
iden = []

for sor in forras:
    adat = sor. strip().split(';')
    tavaly.append(int(adat[0]))
    iden.append(int(adat[1]))

print(iden)
print(tavaly)

forras.close()

idei_max_id = 0
idei_max_magassag = iden[0]

idei_min_id = 0
idei_min_magassag = iden[0]

for i in range(1, len(iden)):
    if iden[i] > idei_max_magassag:
        idei_max_magassag = iden[i]
        idei_max_id = i
    if iden[i] < idei_min_magassag:
        idei_min_magassag = iden[i]
        idei_min_id = i

tavaly_min_id = 0
tavaly_min_magassag = tavaly[0]

tavaly_max_id = 0
tavaly_max_magassag = 0

for i in range(len(tavaly)):
    if tavaly[i] > tavaly_max_magassag:
        tavaly_max_magassag = tavaly[i]
        tavaly_max_id = i
    if tavaly[i] < tavaly_min_magassag:
        tavaly_min_magassag = tavaly[i]
        tavaly_min_id = i

print(f'tavalyi legnagyobbat a {tavaly_max_id} számú versenyző ugrotta: {tavaly_max_magassag}.')
print(f'tavalyi legkisebbet a {tavaly_min_id} számú versenyző ugrotta: {tavaly_min_magassag}.')
print(f'idei legnagyobbat a {idei_max_id} számú versenyző ugrotta: {idei_max_magassag}.')
print(f'idei legkisebbet a {idei_min_id} számú versenyző ugrotta: {idei_min_magassag}.')