def fel(x):
    print(f"{x}. feladat")

napok_száma = input("Adja meg a napok számát! ")
csap_mennyiség = input("Adja meg naponként a csapadék mennyiségét! ")

csapadék = []

for napi in csap_mennyiség.split(" "):
    csapadék.append(int(napi))

#a. feladat
fel("a")

print(len([i for i in csapadék if i>0]))

#b. feladat
fel("b")

száraz = 0


def száraznapok(kezdő_nap):
    nap_sorszáma = kezdő_nap
    while nap_sorszáma < len(csapadék) and csapadék[nap_sorszáma] == 0:
        nap_sorszáma += 1
        return nap_sorszáma - kezdő_nap

for i in range(len(csapadék)):
    if száraznapok(i) > száraznapok(száraz):
        száraz = i
print(száraz)

#c. feladat
fel("c")

legtöbb_csap = 0

for i in range(len(csapadék)-1):
    kettesével = csapadék[i] + csapadék[i+1]
    if kettesével > legtöbb_csap:
        legtöbb_csap = kettesével
print(legtöbb_csap)

