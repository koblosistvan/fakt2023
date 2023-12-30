forrás = open('covid.txt')
dátum = []
regisztrált = []
halott = []
for i in forrás:
    x = i.strip().split(';')
    dátum.append(x[0])
    regisztrált.append(int(x[1]))
    halott.append(int(x[2]))

print('1. feladat')
print(f'Az állomány {len(dátum)} nap adatait tartalmazza.')

print('\n' + '2. feladat')
print(f'A két év alatt összesen {"{:,}".format(sum(regisztrált))} fertőzöttet és {"{:,}".format(sum(halott))} halottat regisztráltak.')

print('\n' + '3. feladat')
sok_alatt = 0
for i in range(len(regisztrált)):
    if regisztrált[i] < 100000:
        sok_alatt += 1
print(f'A fertőzőttek száma {sok_alatt} napon volt 100e fő alatt.')

print('\n' + '4. feladat')
x = halott.index(max(halott))
print(f'Legtöbben {dátum[x]} napon haltak meg:' + '\n' + f'{"{:,}".format(regisztrált[x])} fertőzött' + '\n' +
      f'{"{:,}".format(halott[x])} halott')

print('\n' + '5. feladat')
ind = 0
x = 0
for i in range(len(regisztrált)-1):
    a = regisztrált[i]
    b = regisztrált[i+1]
    if b / a > x:
        x = b / a
        ind = regisztrált.index(regisztrált[i+1])
print(f'A legnagyobb arányú növekedés {dátum[ind]} napon volt, amikor az előző napi adat {round(x, 2)}-szorosa volt a '
      f'fertőzőttek száma.')

print('\n' + '6. feladat')
nő = 0
csökk = 0
for i in range(len(halott)-1):
    if halott[i] < halott[i+1]:
        nő += 1
    if halott[i] > halott[i+1]:
        csökk += 1
print(f'A halálozások száma {csökk} napon csökkent és {nő} nőtt az előző naphoz képest.')

print('\n' + '7. feladat')
print(f'A napi halálozások átlagos száma {"{:,}".format(round(sum(halott) / len(halott), 1))} volt.')
