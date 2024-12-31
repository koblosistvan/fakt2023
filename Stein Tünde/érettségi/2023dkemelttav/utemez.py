# 1
forras = open('taborok.txt', 'r', encoding='utf-8')
honaptol = []
naptol = []
honapig = []
napig = []
azon = []
tabor = []
for sor in forras:
    i = sor.strip().split('\t')
    honaptol.append(int(i[0]))
    naptol.append(int(i[1]))
    honapig.append(int(i[2]))
    napig.append(int(i[3]))
    azon.append(i[4])
    tabor.append(i[5])
forras.close()

# 2
print(f'2. feladat\n'
      f'Az adatsorok száma: {len(honaptol)}\n'
      f'Az először rögzített tábor témája: {tabor[0]}\n'
      f'Az utoljára rögzített tábor témája: {tabor[-1]}')

# 3
zenei = []
for i in range(len(tabor)):
    if tabor[i] == 'zenei':
        zenei.append(i)
print('3. feladat')
if zenei:
    for i in zenei:
        print(f'Zenei tábor kezdődik {honaptol[i]}. hó {naptol[i]}. napján.')
else:
    print('Nem volt zenei tábor.')

# 4
legtobb = len(azon[0])
for i in azon:
    if len(i) > legtobb:
        legtobb = len(i)
print('4. feladat\nLegnépszerűbbek:')
legtobbindex = []
for i in range(len(azon)):
    if len(azon[i]) == legtobb:
        print(f'{honaptol[i]} {naptol[i]} {tabor[i]}')

# 5
def sorszam(kezdoho, kezdonap):
    if kezdoho == 6:
        kezdonap -= 15
    elif kezdoho == 7:
        kezdonap += 30-15
    elif kezdoho == 8:
        kezdonap += 30-15+31
    return kezdonap

# 6
print('6. feladat')
ho = int(input('hó: '))
nap = int(input('nap: '))
taborok_ekkor = []
for i in range(len(honaptol)):
    if sorszam(honaptol[i], naptol[i]) <= sorszam(ho, nap) <= sorszam(honapig[i], napig[i]):
        taborok_ekkor.append(i)
print(f'Ekkor éppen {len(taborok_ekkor)} tábor tart.')

# 7
tanulo = input('Adja meg egy tanuló betűjelét: ')
egytanulo = open('egytanulo.txt', 'w', encoding='utf-8')
kimenet = []
lista7 = []
for i in range(len(azon)):
    if tanulo in azon[i]:
        kimenet.append(f'{honaptol[i]}.{naptol[i]}-{honapig[i]}.{napig[i]}. {tabor[i]}')
        lista7.append([honaptol[i], naptol[i], honapig[i], napig[i]])
kimenet.sort()
for i in kimenet:
    print(i, file=egytanulo)
egytanulo.close()

lista7.sort()
elmehete = 'Elmehet'
for i in range(len(lista7)-1):
    if sorszam(lista7[i][2], lista7[i][3]) > sorszam(lista7[i][0], lista7[i][1]):
        elmehete = 'Nem mehet el'
print(f'{elmehete} mindegyik táborba.')

"""
7. feladat
Adja meg egy tanuló betűjelét: L
Nem mehet el mindegyik táborba. """