import random
forras = open('szavak.txt', mode='r', encoding='utf-8')
szavak = []
for i in forras:
    sor = i.strip('').split(', ')
    for k in range(len(sor)):
        szavak.append(sor[k].strip('""'))
forras.close()
rejtett_index = random.randint(1, len(szavak))
l_rejtett = szavak[rejtett_index]
rejtett = []
for i in l_rejtett:
    rejtett.append(i)
a = True
counter = 0
while a == True:
    counter += 1
    l_tipp = input('Kérem a tippet: ')
    tipp = []
    for i in l_tipp:
        tipp.append(i)
    valasz = ["."]*len(tipp)
    if tipp == "stop":
        a = False
    else:
        for i in range(len(tipp)):
            if tipp[i] == rejtett[i]:
                valasz[i] = tipp[i]
    print(f'Az eredmény: {"".join(valasz)}')
    if '.' not in valasz:
        print(f'{counter} tippeléssel sikerült kitalálni.')