forrás = open("8a-kártyák.txt", mode="r", encoding="utf-8")

lista = []

for sor in forrás:
    adat = sor.strip().split()
    lista.append(int(adat[0]))


#a

for i in range(len(lista), 0 ,-1):
    for j in range(i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]





















