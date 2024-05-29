forras = open('imdb.txt', 'r', encoding='utf-8')
forras.readline()

ev = []
idotartam = []
ertekeles = []
rendezo = []
bevetel = []
cim = []
for i in forras:
    k = i.strip().split('\t')[0]
    ev.append(int(k))
    k = i.strip().split('\t')[1]
    idotartam.append(int(k))
    k = i.strip().split('\t')[2]
    ertekeles.append(float(k))
    rendezo.append(i.strip().split('\t')[3])
    k = i.strip().split('\t')[4]
    bevetel.append(int(k))
    cim.append(i.strip().split('\t')[5])
forras.close()

# task 1
print(f'{len(ev)} film adatai vannak az állományban.')

# task 2
print(f'{min(ev)}-ban/ben jelent meg az első film.')

# task 3
ketoranal = 0
if max(idotartam) > 120:
    for i in idotartam:
        if i > 120:
            ketoranal += 1
    print(f'{ketoranal} két óránál hoszabb film van.')
else:
    print('Nincs két óránál hosszabb film.')

# task 4
for i in ertekeles:
    if i > 9:
        print('Van 9-esnél nagyobb értékelésű film.')
        break
    else:
        print('Nincs 9-esnél nagyobb értékelésű film.')

# task 5
print(f'{max(ertekeles)} a legmagasabb értékelés')

# task 6
ertekeles2 = sorted(list(set(ertekeles)))
ertekeles_lista = []
for i in ertekeles2:
    ertekeles_lista.append(str(ertekeles.count(i)))
print(", ".join(ertekeles_lista))

# task 7
for i in range(len(ertekeles)):
    if ertekeles[i] == ertekeles2[-1]:
        print(f'{rendezo[i]} rendezte legjobb értékelést kapott filmet')

# task 8
input_rendezo = input('> ')
txt = open(f'{input_rendezo.split(" ")[0]}.txt', "w", encoding='utf-8')
for i in range(len(rendezo)):
    if rendezo[i] == input_rendezo:
        print(cim[i], file=txt)
txt.close()

# task 9
ev2 = sorted(set(ev))
osszbevetel = 0
for i in ev2:
    evek = 0
    for k in range(len(ev)):
        if ev[k] == i:
            evek += 1
            osszbevetel += bevetel[k]
    print(f'{i}-ban/ben {evek} film készült, és {osszbevetel} volt a teljes bevétel.')

# taskl 10
print(f'Egy film átlagos bevétele: {sum(bevetel)/len(bevetel)}')

# task 11
print('A 10 legnagyobb bevételű film:')
bevetel2 = bevetel
cim2 = cim
for i in range(len(bevetel2)-1):
    if bevetel2[i] < bevetel2[i+1]:
        bevetel2[i], bevetel2[i+1] = bevetel2[i], bevetel2[i+1]
        cim2[i], cim2[i + 1] = cim2[i], cim2[i + 1]
for i in range(10):
    print(cim2[i])

# task 12
osszfilmek = []
legtobb = 0
for i in rendezo:
    osszfilmek.append(rendezo.count(i))
rendezo2 = rendezo
for i in range(len(osszfilmek)-1):
    if osszfilmek[i] < osszfilmek[i+1]:
        osszfilmek[i], osszfilmek[i+1] = osszfilmek[i], osszfilmek[i+1]
        rendezo2[i], rendezo2[i + 1] = rendezo2[i], rendezo2[i + 1]
print('Az 5 legtöbb filmet rendező neve:')
for i in range(len(rendezo2)):
    ertekelesei = []
    filmjei = []
    for k in range(len(rendezo)):
        if i == rendezo[k]:
            ertekelesei.append(ertekeles[k])
            filmjei.append(cim[k])
    for k in range(len(ertekelesei) - 1):
        if ertekelesei[k] < ertekelesei[k + 1]:
            ertekelesei[k], ertekelesei[k + 1] = ertekelesei[k], ertekelesei[k + 1]
            filmjei[k], filmjei[k + 1] = filmjei[k], filmjei[k + 1]
    print(f'{i} - átlagértékelés: {sum(ertekelesei)/len(ertekelesei)}')
    print('\t' "\n\t".join(filmjei))



