import math
with open("hajok.txt", "r", encoding="utf-8") as f:
    KONTENER_DB, HAJO_CAP = f.readline().strip().split(" ")
    KONTENER_DB, HAJO_CAP = int(KONTENER_DB), int(HAJO_CAP)
    allomasok = []
    for sor in f:
        allomasok.append(sor.strip())
print(allomasok)

hajok_data = []
varosok = set(allomasok)

for varos in varosok:
    temp = allomasok.count(varos)
    kontener_varosba = math.ceil(temp / HAJO_CAP)
    hajo_varosba = temp % HAJO_CAP
    print(f"{varos} {kontener_varosba} {hajo_varosba}")
    hajok_data.append([varos, hajo_varosba, kontener_varosba])

print(hajok_data)
for i in range(len(hajok_data)):
    for j in range(len(hajok_data)):
        if hajok_data[i][2] > hajok_data[j][2]:
            hajok_data[i], hajok_data[j] = hajok_data[j], hajok_data[i]
print(hajok_data)


print("\n-Megoldás: -")
for i in range(3):
    print(f"{hajok_data[i][0]} {hajok_data[i][1]} {hajok_data[i][2]}")