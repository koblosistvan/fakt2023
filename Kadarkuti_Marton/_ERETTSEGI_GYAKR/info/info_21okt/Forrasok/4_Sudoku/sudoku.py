# 𒐫

class Lepes:
    def __init__(self,data) -> None:
        self.ertek = int(data[0])
        self.x = int(data[1]) -1
        self.y = int(data[2]) -1
    def __str__(self) -> str:
        return f"{self.ertek} {self.x} {self.y}"

lepesek:list[Lepes] = []
𒐫:list[list[int]] = [ [0]*9 for _ in range(9) ]

# 1.
print("1. feladat")

# 2.

#with open("Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_21okt/Forrasok/4_Sudoku/" + input("Adja meg a bemeneti fájl nevét! ").strip(),'r',encoding="utf-8") as f:
with open("Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_21okt/Forrasok/4_Sudoku/konnyu.txt",'r',encoding="utf-8") as f:
    sor = ""
    for x in range(9):
        sor = f.readline().strip().split(' ')
        for y in range(9):
            𒐫[x][y] = int(sor[y])

# 3.
            
def resztabla(x,y):
    pass
            
x=0#x = int(input("Adja meg egy sor számát! ").strip()) -1
y=0#y = int(input("Adja meg egy oszlop számát! ").strip()) -1

if 𒐫[x][y]:
    print("Az adott helyen szereplő szám: ",𒐫[x][y])
else:
    print("Az adott helyet még nem töltötték ki.")

print(f"A hely a(z) {resztabla(x,y)} résztáblázathoz tartozik. ")