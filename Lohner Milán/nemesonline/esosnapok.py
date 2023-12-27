napok_szama = input('Add meg az elmult napok szamat: ')
csapadekmennyiseg = input('Add meg a csapadek mennyiseget: ')

csapadek = []

for napi in csapadekmennyiseg.split(' '):
    csapadek.append(int(napi))

#elsofeladat
esosnapok = 0
for i in range(len(csapadek)):
    if csapadek[i] > 0:
        esosnapok += 1

print(esosnapok)


#masodiknaptol hagy napig esett a csapadek

szaraznap = 0

def szaraznapfuggv(kezdonap):
    napsorszam = kezdonap
    while napsorszam < len(csapadek) and csapadek[napsorszam] == 0:
        napsorszam += 1
    return napsorszam - kezdonap


for i in range(len(csapadek)):
    if szaraznapfuggv(i) > szaraznapfuggv(szaraznap):
        szaraznap = i

print(f'{szaraznapfuggv(szaraznap)} száraz nap volt')