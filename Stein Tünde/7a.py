kimenet = open ('arak.txt', mode='w', encoding='utf-8')

print(f'', file=kimenet)
kimenet.close()
forras = open('7a-lakas-arak.txt', mode='r', encoding='utf-8')

forras.readline()
lakasok_alapterulet = []
lakasok_ar = []
for sor in forras:
    adat = sor.strip().split( )
    lakasok_alapterulet.append(int(adat[0]))
    lakasok_ar.append(int(adat[1]))

#1. feladat
legdragabb = 0
for i in range(len(lakasok_ar)):
    if lakasok_ar[i] > legdragabb:
        legdragabb = lakasok_ar[i]
        i_ertek =i

print(f'A legdrágább lakás ára {legdragabb} M Ft, sorszáma {i_ertek + 1}.')

#2. feladat
_500nal_dragabb = False
for i in range(len(lakasok_ar)):
    if lakasok_ar[i] > 500:
        _500nal_dragabb = True

#3. feladat
legmagasabb_arany = 0
for i in range(len(lakasok_ar)):
    if lakasok_ar[i]/lakasok_alapterulet[i] > legmagasabb_arany:
        legmagasabb_arany = lakasok_ar[i]/lakasok_alapterulet[i]
        i_ertek =i
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