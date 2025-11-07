napok_szama = input('Add meg a bementet:')
csapadek_adatok = input('Add meg a csapadék mennyiségét:') #5 0 0 0 0 5 0 3 3 0 0

csapadek = []
for napi in csapadek_adatok.split(' '):
    csapadek.append(int(napi))

#1feladat
esosnapok = 0
for i in range(len(csapadek)):
    if csapadek[i] > 0:
        esosnapok += 1
print(f'{esosnapok} napon esett az eső.')

szaraz = 0

def szaraznapokszama(kezdonap):
    napok_sorszama = kezdonap
    while napok_sorszama < len(csapadek) and csapadek[napok_sorszama] == 0:
        napok_sorszama += 1
    return napok_sorszama - kezdonap

for i in range(len(csapadek)):
    if szaraznapokszama(i) > szaraznapokszama(szaraz):
        szaraz = i

print(f'A leghosszab száraz időszak {szaraznapokszama(szaraz)} nap volt.')


ketnapi_adatok = []
for i in range(len(csapadek)-1):
    ketnapi = csapadek[i] + csapadek[i+1]
    ketnapi_adatok.append(ketnapi)
print(max(ketnapi_adatok))
