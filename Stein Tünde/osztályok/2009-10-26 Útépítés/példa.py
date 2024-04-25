def feladatszam(x):
    print(*'*' * 30, sep=' ')
    print(f'{x}. feladat\n')

def mp_érték(l):
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

forras = open('forgalom.txt', 'r', encoding='utf-8')
forras.readline()
idopontok = []
uthoz_szukseges_ido = []
kiindulas = []

for sor in forras: # beolvasás
    adat = sor.strip().split(' ')
    idopontok.append(mp_érték(adat[:3]))
    uthoz_szukseges_ido.append(int(adat[3]))
    kiindulas.append(adat[4])
forras.close()


sorrend = sorted(uthoz_szukseges_ido)
top10 = sorrend[:10]
kiírt = 0
for idő in set(top10):
    for i in range(len(uthoz_szukseges_ido)):
        if uthoz_szukseges_ido[i] == idő:
            belépés = f'{idopontok[i] // 3600:02d}:{idopontok[i] % 3600 // 60:02d}:{idopontok[i] % 60:02d}'
            print(f'Belépés {kiindulas[i]} irányból: {belépés}; Sebesség: {3600/uthoz_szukseges_ido[i]:.2f} m/s')
            kiírt += 1
            if kiírt == 10:
                break

