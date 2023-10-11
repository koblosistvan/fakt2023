import cuccok
forrás = open('6b.txt', mode='r', encoding='utf8')
cuccok.vonal()
hely = []
idopont = []

forrás.readline()
for sor in forrás:
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    idopont.append(int(adat[1]) * 60 + int(adat[2]))
forrás.close()

leghosszabb_id = 0
leghosszabb_ido = idopont[1] - idopont[0]
for i in range(len(hely)-1):
    if idopont[i+1] - idopont[i] > leghosszabb_ido:
        leghosszabb_id = i
        leghosszabb_ido = idopont[i+1] - idopont[i]

ötvenespontok = 0
for i in range(len(hely)):
    if hely[i] == 50:
        ötvenespontok += 1

print(f'{ötvenespontok} adat tartozik az 50es mérési ponthoz')
cuccok.vonal()

bekért = int(input('időpont:'))



