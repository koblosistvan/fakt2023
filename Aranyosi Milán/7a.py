kimenet = open('arak.txt', mode='w', encoding='utf8')

print(f'Eddig is írtunk ilyet.', file=kimenet)

kimenet.close()

forras = open('7a-lakas-arak.txt', mode='r', encoding='utf8')
meret = []
ar = []

forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    meret.append(int(adat[0]))
    ar.append(int(adat[1]))
forras.close()
print(ar)
print(meret)

def vonal():
    print('-'*100)

#1. feladat
legdragabb = ar[0]
legdragabb_id = 0
for i in range(len(ar)):
    if ar[i] > legdragabb:
        legdragabb = ar[i]
        legdragabb_id = i
print(f'A legdragabb ház {legdragabb} millió forintba kerül, {legdragabb_id} a sorszáma.')
vonal()

#2.feladat
for i in range(len(ar)):
    if ar[i] > 500:
        print('Van 500 milliónál drágább ház.')
        break
else:
    print('Nincs 500M forintnál dgágább ház.')
vonal()

#3.feladat
legjobb_arany = ar[0] / meret[0]
for i in range(len(ar)):
    if ar[i] / meret[i] > legjobb_arany:
        legjobb_arany = ar[i] / meret[i]
        legjobb_arany_id = i
print(f'A legjobb arányú ház a {legjobb_arany_id} számú ház ennek aránya: {legjobb_arany}')
vonal()

#4. feladat
huszalatti = 0
for i in range(len(ar)):
    if ar[i] < 20:
        huszalatti += 1
print(f'{huszalatti} darab 20 millió Ft alatti ingatlan van.')
vonal()

#5. feladat
otven_hatvan_kozotti = []
otven_hatvan_kozotti_ar = []
for i in range(len(meret)):
    if 50 < meret[i] < 60:
        otven_hatvan_kozotti.append(meret[i])
        otven_hatvan_kozotti_ar.append(ar[i])
kimenet = open('arak.txt', mode='w', encoding='utf-8')
print(f'Az 50 négyzetméter és a 60 négyzetméteres házak listája: {otven_hatvan_kozotti} (négyzetméter) \nárainak listája: {otven_hatvan_kozotti_ar} (millió Ft)', file=kimenet)
kimenet.close()

#6.feladat
print('Figyelj arra, hogy ne ugyanazt az értéket add meg és az egyes helyekre csak egy számot adj meg.')
ar_tartomanymin = input('Add meg aza also hatart:')
ar_tartomanymax = input('Add meg a felső határt:')
keresett_hazak_id = []
kimenet = open('arak.txt', mode='w', encoding='utf-8')
for i in range(len(ar)):
    if int(ar_tartomanymin) < ar[i] < int(ar_tartomanymax):
        keresett_hazak_id.append(i)
print(f'\n\n\n\nSzámodra a {keresett_hazak_id} sorszámú házak lesznek a megfelelők.', file=kimenet)
kimenet.close()

#7.feladat

