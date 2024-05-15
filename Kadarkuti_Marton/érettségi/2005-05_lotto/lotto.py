hetenteList = []
# 0.
with open("lottosz.dat", "r") as f:
    for sor in f:
        hetenteList.append(list(map(int, list(sor.strip().split(" ")))))
#print(hetente)

# 1.

try:
    print("    # 89 24 34 11 64")
    otvenkettoInput = input("Add meg vesszővel elválasztva!\n> ").split(" ")
    otvenkettoInput = list(map(int, otvenkettoInput))
    # 2.
    otvenkettoInput = sorted(otvenkettoInput)
    otvenkettoOutput = " ".join(map(str, otvenkettoInput))
    print(f"Bemenet: \n    {otvenkettoOutput}")
except:
    print("Érvénytelen bemenet.")
    quit()

# 3.
sorszamInput = int(input("Adj meg egy sorszámot 1-51 között:\n> "))
sorszamOutput = " ".join(map(str, hetenteList[sorszamInput - 1]))
# 4.
print(f"{sorszamInput}. hét nyerő számai:\n    {sorszamOutput}")

# 5.
hetenteSet = []
for i in range(len(hetenteList)):
    hetenteSet += hetenteList[i]
hetenteSet += otvenkettoInput
hetenteSet = set(hetenteSet)
print("\n# 5. feladat:")
if len(hetenteSet) == 99:
    print("  Nincs")
else:
    print("  Van")

# 6.
paratlanokSzama = 0
for i in range(len(hetenteList)):
    for j in range(5):
        if hetenteList[i][j] % 2 == 1:
            paratlanokSzama += 1
for i in range(5):
    if otvenkettoInput[i] % 2 == 1:
        paratlanokSzama += 1

print(f"\n{paratlanokSzama} alkalommal lett kihúzva páratlan szám.")

# 7.
hetenteList.append(otvenkettoInput)

f = open("lotto52.ki", "w")
f.close()
with open("lotto52.ki", "a"):
    for i in range(len(hetenteList)):
        sor = " ".join( map(str, hetenteList[i]) )
        f.write(sor)