# Nemes Tihamér Online 2. forduló - 1. feladat - DNS Darabok
# Kadarkuti Márton

tmp = "" # seged
dns_hossz:int = 0
sorok_szama:int = 0
bemenet_kezdoszamok:list[int] = []
bemenet_sorok:list[str] = []
teljes_bemenet:str = ""

tmp = input().strip().split(' ') # elso sor
dns_hossz = int(tmp[0])
sorok_szama = int(tmp[1])

for sor in range(sorok_szama):
    sor = input() 
    tmp = sor.strip().split(' ')
    bemenet_kezdoszamok.append( int(tmp[0]) -1)
    bemenet_sorok.append(tmp[1])

for sor in bemenet_sorok:
    teljes_bemenet += sor

kimenet:list[str] = list( "?"*dns_hossz )
jelen_sor:int = 0
i:int = 0

for j in bemenet_kezdoszamok:
    for betu in bemenet_sorok[jelen_sor]:
        if kimenet[i+j] != '?' and kimenet[i+j] != betu:
            # ellentmondas
            print("Hiba!")
            quit()
        kimenet[j+i] = betu
        i+=1
    i = 0
    jelen_sor += 1
    
# helyes kimenet
print(''.join(kimenet))

