forras = open('valaszok.txt', mode='r', encoding='utf-8')
versenyzok = []
valaszok = []
helyesvalasz = forras.readline()

for i in forras:
    sor = i.strip().split(' ')
    versenyzok.append(str(sor[0]))
    valaszok.append(str(sor[1]))
forras.close()
versenyzok.pop(0)
valaszok.pop(0)
print(f'2. feladat: {len(versenyzok)}')
v_az = str(input('Adja meg egy versenyző azonosítóját: '))
print(valaszok[versenyzok.index(v_az)])