hetenteList = []
# 0.
with open("lottosz.dat", "r") as f:
    for sor in f:
        hetenteList.append(list(map(int, list(sor.strip().split(" ")))))
#print(hetente)

# 1.

try:
    print("    # 89 24 34 11 64")
    otvenkettoInput = input("Add meg szóközzel elválasztva!\n> ").split(" ")
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


f = open("lotto52.ki", "w")  # üreset generál
f.close()
with open("lotto52.ki", "a") as f:
    for i in range(len(hetenteList)):
        sor = " ".join( map(str, hetenteList[i]) ) + "\n"
        f.write(sor)

# 8.
adattabla = [0]*90
hetenteUnsorted = []
for i in range(len(hetenteList)):
    for j in range(len(hetenteList[i])):
        hetenteUnsorted.append(hetenteList[i][j])
for i in range(len(hetenteUnsorted)):
    adattabla[ hetenteUnsorted[i] -1 ] += 1

print("\n# 8. feladat:")
for sor in range(6):
    tempTxt = "   "
    for i_sor in range(15):
        tempTxt += str( adattabla[ 15*sor + i_sor ] ) + " "
    print(tempTxt)

# 9.
def is_prime(n): # n>1 (egész n) bemenetre helyes a kimenet
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n/2)+1, 2):
        if n%i == 0:
            return False
    return True
primek_kilencvenig = []
for i in range(2,90):
    if is_prime(i):
        primek_kilencvenig.append(i)

kilencesFeladatKimenet = []
for i in range(len(primek_kilencvenig)):
    temp = primek_kilencvenig[i]
    if adattabla[ temp -1 ] == 0:
        kilencesFeladatKimenet.append(temp)

print("\n# 9. feladat:")
if not bool(kilencesFeladatKimenet):
    print("Minden prímszám legalább egyszer ki lett húzva.")
else:
    temp = ", ".join( map( str, kilencesFeladatKimenet ) )
    print(f"Egyszer sem kihúzott prímek: { temp }.")
