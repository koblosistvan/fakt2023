lista = []
i = 0
while True:
    szo = input(f'{i+1}. szó: ')
    if len(szo) != 6:
        print('A karakterek száma téves!')
        break
    if i != 0 and szo[0] != lista[-1][-1]:
        print('Nem illeszkedett!')
        break
    lista.append(szo)
    i += 1
if i <= 2:
    szint = 'kezdo'
elif i <= 5:
    szint = 'kozepes'
else:
    szint = 'halado'
print(f'Helyes lépések száma: {i}\nSzint: {szint}')
