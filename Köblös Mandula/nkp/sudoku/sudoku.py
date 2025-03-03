forrás = open('sudoku_mo.txt', mode='r', encoding='utf-8')

megoldas = []

for sor in forrás:
    adat = sor.strip()
    megoldas.append(adat)

forrás.close()

forrás2 = open('sudoku_jatekos1.txt', mode='r', encoding='utf-8')

jatekose = []

for sor in forrás2:
    adat = sor.strip()
    jatekose.append(adat)

forrás2.close()


for szam in jatekose:
    for szam2 in megoldas:
        if szam != szam2:
            print('Nem jó a megoldás')
            break