import math
forrás = open("hajok.txt", mode="r", encoding="utf-8")

elso_sor = forrás.readline().strip().split(" ")
max_konténer = int(elso_sor[1])


konténerek = []

for sor in forrás:
    adat = sor.strip()
    konténerek.append(adat)

városok = set(konténerek)
eddigi_városok = {}

for város in városok:
    városba = konténerek.count(város)
    print(f"{város} {math.ceil(városba/max_konténer)} üres helyek száma")





"""for i in range(len(konténerek)):
    if konténerek[i] not in eddigi_városok:
        eddigi_városok.append()"""

















