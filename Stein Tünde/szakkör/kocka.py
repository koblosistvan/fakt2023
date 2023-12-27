forras = open('kocka.txt', 'r', encoding='utf-8')

listalista = []
for i in forras:
    adat = i.strip().split('\t')
    listalista.append(adat)
forras.close()
bemenet = input('> ').split(' ')

for i in range(len(bemenet)-1):
    ellenorzes = [bemenet[i], bemenet[i+1]]
    if ellenorzes not in listalista:
        print('Nem bejárható.')
        break
else:
    print('Bejárható.')
