szamok = []

for i in range(10):
    szam = int(input(f'{i+1}. szám: '))
    szamok.append(szam)

print(f'Eredeti lista: {szamok}')

for i in range(len(szamok) - 1):
    min = i
    for j in range(i + 1, len(szamok)):
        if szamok[j] < szamok[min]:
            min = j

    seged = szamok[i]
    szamok[i] = szamok[min]
    szamok[min] = seged


print(f'növekvő sorrendű lista: {szamok}')
