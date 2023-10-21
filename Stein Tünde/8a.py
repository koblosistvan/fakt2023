forras = open('8a-kártyák.txt', 'r', encoding='utf-8')
lista = []
for i in forras:
    adat = i.strip().split()
    lista.append(int(adat[0]))
print(lista)

for i in range(len(lista), 0, -1):
    for k in range(i-1):
        if lista[k] > lista[k+1]:
            lista[k], lista[k+1] = lista[k+1], lista[k]
            print(lista)