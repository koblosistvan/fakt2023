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
ertekeles2 = sorted(set(ertekeles))
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
txt = open(f'{input_rendezo.split(" ")[0].lower}.txt', "w", encoding=utf-8)
for i in range(len(rendezo)):
    if rendezo[i] == input_rendezo:
        print(cim[i], file=txt)

# task 9
ev2 = sorted(set(ev))
evek = 0
osszbevetel = 0
for i in ev2:
    for k in range(len(ev)):
        if ev[k] == i:
            evek += 1
            osszbevetel += bevetel[k]
    print(f'{i}-ban/ben {evek} film készült, és {osszbevetel} volt a teljes bevétel.')
    ev_lista.append(str(ev.count(i)))
print(", ".join(ev_lista))

