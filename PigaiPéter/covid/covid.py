forras = open('covid.txt', mode='r', encoding='utf-8')
datum = []
fertozes = []
halalozas = []
for i in forras:
    sor = i.strip().split(';')
    datum.append(sor[0])
    fertozes.append(int(sor[1]))
    halalozas.append(int(sor[2]))
#1
print(len(datum))

#2
print(f'A halálozások:{sum(halalozas)}, a regisztrált fertőzések:{sum(fertozes)}')

#3
alatt = 0
for i in range(len(fertozes)):
    if fertozes[i] < 100000:
        alatt += 1
print(f'{alatt} alkalommal volt 100e alatt a napi fertőzöttség')

#4
legtobb = 0
for i in range(len(halalozas) - 1):
    if halalozas[i] > legtobb:
        legtobb = halalozas[i]
print(f'{legtobb} volt a legtöbb napi halálozás, emellett {fertozes[halalozas.index(legtobb)]} fertőzés történt')

#5
rata = 0
ind = 0
for i in range(len(fertozes) - 1):
    if rata < fertozes[i + 1] / fertozes[i]:
        rata = fertozes[i + 1] / fertozes[i]
        ind = fertozes.index(fertozes[i + 1])
print(f'A legnagyobb fertőzöttségi ráta {rata} volt a {datum[ind]}. napon')

#6
csokk = 0
no =  0
for i in range(len(halalozas) - 1):
    if halalozas[i + 1] > halalozas[i]:
        no += 1
    else:
        csokk += 1
print(f'{csokk} napon csökkent, {no} napon nőtt')

#7
print(f'Halálozások napi átlaga: {sum(halalozas)/len(halalozas)}')
