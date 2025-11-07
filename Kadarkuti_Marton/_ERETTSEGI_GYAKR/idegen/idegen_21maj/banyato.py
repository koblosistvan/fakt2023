PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/idegen/idegen_21maj/e_infmafor_21maj_fl/4_Banyato/"

# 1. 
melysegek = []
SOR = 0
OSZLOP = 0
with open(PATH+"melyseg.txt",'r') as f:
    SOR = int(f.readline())
    OSZLOP = int(f.readline())
    for sor in f:
        melysegek.append(list(map(int, sor.strip().split(' '))))

# 2. 
print("2. feladat")
y = int(input("A mérés sorának azonosítója=")) -1
x = int(input("A mérés oszlopának azonosítója=")) -1
print("A mért mélység az adott helyen", melysegek[y][x] , "dm ")

# 3. 
print("3. feladat")
felszin = 0
atl_melyseg = 0
for i in range(SOR):
    for j in range(OSZLOP):
        if melysegek[i][j]:
            felszin += 1
            atl_melyseg += melysegek[i][j]
atl_melyseg = atl_melyseg/(10*felszin) # a felszin meterben van, a melyseg viszont dm-ben

# formatting
atl_melyseg = round(atl_melyseg,2)
atl_melyseg = ','.join(str(atl_melyseg).split('.'))

print(f"A tó felszíne: {felszin} m2, átlagos mélysége: {atl_melyseg} m")

# 4. 
maximum = [0,0]
# megkeres egy maximumot
for i in range(SOR):
    for j in range(OSZLOP):
        if melysegek[i][j] > melysegek[maximum[0]][maximum[1]]:
            maximum = [i,j]

maxok = []

# megkeresi az osszes azonos melysegut
for i in range(SOR):
    for j in range(OSZLOP):
        if melysegek[i][j] == melysegek[maximum[0]][maximum[1]]:
            maxok.append(f"({i+1}; {j+1})")

print("4. feladat")
print(f"A tó legnagyobb mélysége: {melysegek[maximum[0]][maximum[1]]} dm")
print("A legmélyebb helyek sor-oszlop koordinátái:")
print('\t'.join(maxok))

# 5. 
kerulet = 0
for i in range(SOR-1):
    for j in range(OSZLOP-1):
        if not melysegek[i][j]:
            if melysegek[i+1][j]:
                kerulet += 1
            if melysegek[i][j+1]:
                kerulet += 1
        else:
            if not melysegek[i+1][j]:
                kerulet += 1
            if not melysegek[i][j+1]:
                kerulet += 1

print("5. feladat")
print(f"A tó partvonala {kerulet} m hosszú ")

# 6. 
print("6. feladat")
y = int(input("A vizsgált szelvény oszlopának azonosítója=")) -1

with open(PATH+"diagram.txt",'w',encoding="utf-8") as x:
    for i in range(SOR):
        x.write(f"{i+1:02d}{'*'*int(round(melysegek[i][y]/10,0))}\n")