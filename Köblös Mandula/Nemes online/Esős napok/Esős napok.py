napok = input("Napok száma: ")
csapadék_adatok = input("Csapadék mennyisége: ")
#11
#5 0 0 0 0 5 0 3 3 0 0

csapadék = []
for napi in csapadék_adatok.split(" "):
    csapadék.append(int(napi))

print(csapadék)

print("a.feladat")
esett = 0
for i in range(len(csapadék)):
    if csapadék[i] > 0:
        esett += 1
print(f'{esett} napon esett az eső.')

print("b.feladat")
száraz = 0
def száraz_napok_száma(kezdőnap):
    nap_sorszám = kezdőnap
    while nap_sorszám < len(csapadék) and csapadék[nap_sorszám] == 0:
        nap_sorszám += 1
    return nap_sorszám - kezdőnap

for i in range(len(csapadék)):
    if száraz_napok_száma(i) > száraz_napok_száma(száraz):
        száraz = i
print(f'A leghosszabb csapadékmentes időszak {száraz_napok_száma(száraz)} nap volt.')

print("c.feladat")
legtöbb = 0
for i in range(len(csapadék)-1):
    if csapadék[i] + csapadék[i+1] > legtöbb:
        legtöbb = csapadék[i] + csapadék[i+1]
print(legtöbb)