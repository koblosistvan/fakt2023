forras = open('5a-magasugras2.txt', mode='r', encoding='utf-8')

tavalyi = []
iden = []

for sor in forras:
    adat = sor. strip().split(';')
    tavalyi.append(int(adat[0]))
    iden.append(int(adat[1]))

print(iden)
print(tavalyi)

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
tavaly_min_magassag = tavalyi[0]

tavaly_max_id = 0
tavaly_max_magassag = 0

for i in range(len(tavalyi)):
    if tavalyi[i] > tavaly_max_magassag:
        tavaly_max_magassag = tavalyi[i]
        tavaly_max_id = i
    if tavalyi[i] < tavaly_min_magassag:
        tavaly_min_magassag = tavalyi[i]
        tavaly_min_id = i

print(f"Az idei legnagyobbat {idei_max_id} ugrotta {idei_max_magassag} legkisebbet {idei_min_id} ugrotta {idei_min_magassag}")
print(f"A tavalyi legnagyobbat {tavaly_max_id} ugrotta {tavaly_max_id} a legkisebbet {tavaly_min_id} ugrotta {tavaly_min_magassag}")