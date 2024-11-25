hetek = int(input('Hetek száma='))
kivant = float(input('Elérni kívánt testtömeg (kg) ='))
lista = []
counter = 0
for i in range(hetek):
    n_edik = float(input(f'{i+1}. héten='))
    if i != 0 and n_edik > lista[-1]:
        counter += 1
    lista.append(n_edik)
a = 0
for i in range(len(lista)):
    if lista[i] <= kivant:
        a = i + 1
        break
if bool(a):
    print(f'Mari néni a(z) {a}. héten érte el a célt.')
else:
    print('Sajnos Mari néni nem érte el a célját.')
print(f'A tömege {counter} esetben nőtt egyik hétről a másikra.')