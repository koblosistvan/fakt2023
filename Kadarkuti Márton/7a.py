forras = open("7a-lakas-arak.txt", "r", encoding="utf-8")
forras.readline() #rossz sor

teruletek = []
arak = []
for sor in forras:
    adat = sor.strip().split(' ')
    teruletek.append(int(adat[0]))
    arak.append(int(adat[1]))
forras.close()

print(teruletek)
print(arak)
