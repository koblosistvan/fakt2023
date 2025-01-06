PATH:str = "C:\\xampp\\htdocs\\fakt2023\\fakt2023\\Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\23maj22info\\Forras\\4_RGBszinek\\kep.txt"

class Pixel:
    VILAGOSAK_SZAMA:int = 0
    LEGSOTETEBB_OSSZEG:int = 1000
    def __init__(self, red, green, blue):
        self.r = int(red)
        self.g = int(green)
        self.b = int(blue)

        # 3. feladat:
        if self.osszeg() > 600:
            Pixel.VILAGOSAK_SZAMA += 1
        
        # 4. feladat
        if Pixel.LEGSOTETEBB_OSSZEG > self.osszeg():
            Pixel.LEGSOTETEBB_OSSZEG = self.osszeg()

    def __str__(self):
        return f"RGB({self.r},{self.g},{self.b})"
    def osszeg(self):
        return self.r+self.g+self.b
    
# 1.
pixelek:list[list[Pixel]] = [list() for _ in range(360)]
tmp = ""

with open(PATH,'r',encoding="utf-8") as f:
    jelen_sor:int = 0
    for sor in f:
        tmp = sor.strip().split(' ')
        for i in range(640):
            pixelek[jelen_sor].append( Pixel(tmp[3*i], tmp[3*i+1], tmp[3*i+2]) )
        jelen_sor += 1

# 2.
print("2. feladat:")
print("Kérem egy képpont adatait:")
prompt_sor:int = int( input("Sor: ").strip() ) -1
prompt_oszlop:int = int( input("Oszlop: ").strip() ) -1
print("A képpont színe:",pixelek[prompt_sor][prompt_oszlop])

# 3.
print("3. feladat:")
print("A világos képpontok száma:",Pixel.VILAGOSAK_SZAMA)

# 4.
print("4. feladat:")
print("A legsötétebb pont RGB összege:",Pixel.LEGSOTETEBB_OSSZEG)
for sor in range(360):
    for oszlop in range(640):
        if pixelek[sor][oszlop].osszeg() == Pixel.LEGSOTETEBB_OSSZEG:
            print(pixelek[sor][oszlop])

# 5.
def hatar(sor:int, elteres:int)->bool:
    sor -= 1 # indexkorrekcio
    for oszlop in range(640 -1):
        if elteres < abs( pixelek[sor][oszlop].b - pixelek[sor][oszlop+1].b ):
            return True
    return False

# 6.
print("6. feladat:")
elteres_hatar:int = 10

felho_sorok:list[int] = []
for sor in range(360):
    if hatar(sor, elteres_hatar):
        felho_sorok.append(sor)

print("A felhő legfelső sora:",felho_sorok[0])
print("A felhő legalsó sora:",felho_sorok[-1])