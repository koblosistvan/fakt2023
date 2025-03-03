# 1. feladat
forras = open('dobasok.txt', 'r', encoding='utf-8')
lista = []
for i in forras:
    sor = i.strip().split(', ')
    for k in sor:
        lista.append(int(k))
forras.close()

print('2. feladat')
mezok = []
counter = 0
for i in range(len(lista)):
    if i == 0:
        mezok.append(lista[i])
    elif (lista[i]+mezok[-1]) % 10 == 0:
        mezok.append(lista[i] + mezok[-1]-3)
        counter += 1
    else:
        mezok.append(lista[i]+mezok[-1])
for i in mezok:
    print(i, end=' ')

print(f'\n3. feladat\n'
      f'A játék során {counter} alkalommal lépett létrára.')
print('4. feladat')
if mezok[-1] >= 45:
    print('A játékot befejezte.')
else:
    print('A játékot abbahagyta.')
