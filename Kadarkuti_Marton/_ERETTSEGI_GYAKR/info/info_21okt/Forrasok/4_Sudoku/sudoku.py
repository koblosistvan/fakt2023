class Lepes:
    def __init__(self,data) -> None:
        self.ertek = int(data[0])
        self.x = int(data[1]) -1
        self.y = int(data[2]) -1
    def __str__(self) -> str:
        return f"A kiválasztott sor: {1+self.x} oszlop: {1+self.y} a szám: {self.ertek} "
    
    def get_resztabla(self):
        return resztabla(self.y, self.x) # felcsereltem az xy-t
    
lepesek:list[Lepes] = []
𒐫:list[list[int]] = [ [0]*9 for _ in range(9) ]

# 1.
print("1. feladat")

# 2.
negyes_fela_nullasok = 0

with open("Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_21okt/Forrasok/4_Sudoku/" + input("Adja meg a bemeneti fájl nevét! ").strip(),'r',encoding="utf-8") as f:
    sor = ""
    for x in range(9):
        sor = f.readline().strip().split(' ')
        for y in range(9):
            𒐫[x][y] = int(sor[y])

            if not int(sor[y]):
                negyes_fela_nullasok += 1

    for sor in f:
        lepesek.append(Lepes(sor.strip().split(' ')))

# 3.
            
def resztabla(x,y): # nagyon rossz megoldas
    if x in (0,1,2):
        if y in (0,1,2):
            return 1
        elif y in (3,4,5):
            return 4
        else:
            return 7
    elif x in (3,4,5):
        if y in (0,1,2):
            return 2
        elif y in (3,4,5):
            return 5
        else:
            return 8
    else:
        if y in (0,1,2):
            return 3
        elif y in (3,4,5):
            return 6
        else:
            return 9
            
x = int(input("Adja meg egy sor számát! ").strip()) -1
y = int(input("Adja meg egy oszlop számát! ").strip()) -1
cella = 𒐫[x][y]

if cella:
    print("Az adott helyen szereplő szám: ",cella)
else:
    print("Az adott helyet még nem töltötték ki.")

print(f"A hely a(z) {resztabla(x,y)} résztáblázathoz tartozik. ")


# 4.
print(f"Az üres helyek aránya: {(negyes_fela_nullasok/81):.1%}")

# 5.

def get_oszlop(y)->list[int]:
    arr = []
    for i in range(9):
        arr.append(𒐫[i][y])
    return arr

def get_sor(x)->list[int]:
    arr = []
    for i in range(9):
        arr.append(𒐫[x][i])
    return arr

def get_resztabla(n)->list[int]:
    n = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)][n-1] # ez is
    arr = []
    for i in range(9):
        arr.append( 𒐫[n[0] + i//3][n[1] + i%3] )
    return arr


for lepes in lepesek:
    print(lepes)
    cella = 𒐫[lepes.x][lepes.y]

    if cella:
        print("A helyet már kitöltötték")
    elif get_sor(lepes.x).count(lepes.ertek):
        print("Az adott sorban már szerepel a szám")
    elif get_oszlop(lepes.y).count(lepes.ertek):
        print("Az adott oszlopban már szerepel a szám")
    elif get_resztabla( lepes.get_resztabla() ).count(lepes.ertek):
        print("Az adott résztáblázatban már szerepel a szám")
    else:
        print("A lépés megtehető")
    print("")


