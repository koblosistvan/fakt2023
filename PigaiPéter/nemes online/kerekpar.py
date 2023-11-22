forras = open('kerekparverseny.txt', mode='r', encoding='utf-8')
szakaszok = []
forras.readline()
for sor in forras:
    sor = sor.strip()
    szakaszok.append(sor)
jo = []
táv = 0
while táv != 50 or táv > 50:
    táv = szakaszok[0] + szakaszok
print(jo)