text = list(input('Szöveg: ').upper())
karakterek = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ékezetes = 'ÁÉÍÓÖŐÚÜŰ'
ékezetlen = 'AEIOOOUUU'
szöveg = []
for i in range(len(text)):
    if text[i] in ékezetes:
        text[i] = ékezetlen[ékezetes.index(text[i])]
    if text[i] in karakterek:
        szöveg.append(text[i])
print(''.join(szöveg))

kulcsszó = input('Kulcsszó: ').upper()
kulcsszó = kulcsszó*((len(szöveg) // len(kulcsszó))+1)
kulcsszó = kulcsszó[:len(szöveg)]
print(kulcsszó)

forrás = open('Vtabla.dat')
sor = []
kód = []
for i in forrás:
    sor.append(list(i.strip()))
for i in range(len(szöveg)):
    x = karakterek.index(szöveg[i])
    y = karakterek.index(kulcsszó[i])
    kód.append(sor[y][x])
print(''.join(kód))
