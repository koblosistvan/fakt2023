forras = open('5a-magasugras2.txt', mode='r', encoding='utf-8')


magassag = []
idei = []
tavalyi = []

for sor in forras:
    adat = sor.strip().split(';')
    magassag.append(int(adat[0]))
    idei.append(int(adat[1]))

print(magassag)
print(idei)



forras.close()




idei_max_id = 0
idei_max_magassag = idei[0]


for i in range(1, len(idei)):
    if idei[i] > idei_max_magassag:
        idei_max_magassag = idei[i]
        idei_max_id = i


print(f'A legnagyobb idén {idei_max_id} ugrotta {idei_max_magassag}m-t')


idei_min_id = 0
idei_min_hossz = idei[0]


for i in range(1, len(idei)):
    if idei[i] < idei_min_hossz:
        idei_min_hossz = idei[i]
        idei_min_id = i

print(f'A legkisebb idén {idei_min_id} ugrotta {idei_min_hossz}m-t')


tavaly_min_id = 0
tavaly_min_hossz = tavalyi[0]

tavaly_max_id = 0
tavaly_max_hossz = 0





for i in range(1, len(tavalyi)):
    if tavalyi[i] > tavaly_min_hossz:
        tavaly_min_hossz = tavalyi[i]
        tavaly_min_id = i


print(tavaly_min_hossz,tavaly_min_id)



