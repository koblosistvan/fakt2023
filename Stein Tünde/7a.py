kimenet = open ('arak.txt', mode='w', encoding='utf-8')

print(f'', file=kimenet)
kimenet.close()
forras = open('7a-lakas-arak.txt', mode='r', encoding='utf-8')

forras.readline()
lakasok_alapterulet = []
lakasok_ar = []
for sor in forras:
    adat = sor.strip().split(' ')
    lakasok_alapterulet.append(int(adat[0]))
    lakasok_ar.append(int(adat[1]))

#1. feladat
legdragabb = max(lakasok_ar)
legdragabb_index = lakasok_ar.index(legdragabb) + 1
print(f'A legdrágább lakás ára {legdragabb} M Ft, sorszáma {legdragabb_index}.')

#2. feladat
_500nal_dragabb = "Nincs"
for i in range(len(lakasok_ar)):
    if lakasok_ar[i] > 500:
        _500nal_dragabb = "Van"
print(f'{_500nal_dragabb} 500M-nál drágább ingatlan.')

#3. feladat
legmagasabb_arany = 0
for i in range(len(lakasok_ar)):
    if lakasok_ar[i]/lakasok_alapterulet[i] > legmagasabb_arany:
        legmagasabb_arany = lakasok_ar[i]/lakasok_alapterulet[i]
        i_ertek = i
print(f'A {i_ertek + 1}. lakásnak a legnagyobb az ár/terület aránya: {legmagasabb_arany}.')

#4. feladat
_20malatt = 0
for i in range(len(lakasok_ar)):
    if lakasok_ar[i] < 20:
        _20malatt +=1
print(f'{_20malatt} db 20 millió alatti ingatlan van.')

#5. feladat
_50_es_60_kozott = []
for i in range(len(lakasok_alapterulet)):
    if 50 < lakasok_alapterulet[i] < 60:
        _50_es_60_kozott.append(lakasok_alapterulet[i])
kimenet = open ('arak.txt', mode='w', encoding='utf-8')
print(_50_es_60_kozott, file=kimenet)
kimenet.close()

#6. feladat
ar_tartomany = input('Adj meg egy ár tartományt (millió forintban): ')
ar_tartomany = ar_tartomany.strip().split('-')
ar_tartomany1 = int(ar_tartomany[0])
ar_tartomany2 = int(ar_tartomany[1])
talalatok = []
for i in range(len(lakasok_ar)):
    if ar_tartomany1 <= lakasok_ar[i] <= ar_tartomany2:
        talalatok.append(lakasok_ar[i])
print(f'A találatok a megadott tartományra: {talalatok}')

#7. feladat
bekert_adatok = input('Adj meg egy felület és egy árértéket: ')
bekert_adatok = bekert_adatok.strip().split(', ')
felulet, ar = int(bekert_adatok[0]), int(bekert_adatok[1])
talalatok = []
for i in range(len(lakasok_ar)):
    if felulet == lakasok_alapterulet[i] and ar == lakasok_ar[i]:
        talalatok.append(i)
if bool(talalatok):
    for i in range(len(talalatok)):
        print(f'Találatok: {lakasok_alapterulet[talalatok[i]]} négyzetméter, {lakasok_ar[talalatok[i]]} millió forint. ~ {talalatok[i] + 1}. találat.')
else:
    print('Nincs találat.')
