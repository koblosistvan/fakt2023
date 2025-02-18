forrás = open("bank_adatok.txt", mode="r", encoding="utf-8")

beépések = forrás.readline().split(" ")

azon = []
nap = []

for sor in forrás:
    adat = sor.strip().split(" ")
    azon.append(int(adat[0]))
    nap.append(int(adat[1]))

dolgozo_azonok = set(azon)

for dolgozo in dolgozo_azonok:
    print(f"Az {dolgozo} ennyiszer lépett be: {azon.count(dolgozo)}")


"""lista = []
lista_dolgozo_azonok = list(dolgozo_azonok)"""

"""for i in range(len(lista_dolgozo_azonok)):
    lista.append(0)

for i in range(len(azon)):
    
    for j in range(len(dolgozo_azonok)):
        lista[j]"""

mindketten = []

for day in set(nap):
    print(day, end=" ")
    belépők = 0
    for dolgozo in dolgozo_azonok:
        belépés_számok = 0
        for i in range(len(azon)):
            if azon[i] == dolgozo and day == nap[i]:
                belépés_számok += 1
        print(belépés_számok, end=" ")
        if belépés_számok > 0:
            belépők += 1
        if belépők == set(azon):
            mindketten.append(day)
    print()


print(mindketten)






