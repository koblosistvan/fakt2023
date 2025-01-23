INPUT_PATH:str = "Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_22okt/Informatika_forras_E2212/4_Jelado/jel.txt"

def ido_format(t:int)->str:
    return f"{t//3600}:{t//60}:{t%60}"

class Jel:
    def __init__(self, data) -> None:
        self.ora = int(data[0])
        self.perc = int(data[1])
        self.mp = int(data[2])
        self.x = int(data[3])
        self.y = int(data[4])
    def __str__(self) -> str:
        return f"{self.ora} {self.perc} {self.mp} {self.x} {self.y}"
    
    def get_mp(self)->int:
        return self.ora*3600 + self.perc*60 + self.mp


# 1.
jelek:list[Jel] = []
with open(INPUT_PATH, 'r', encoding="utf-8") as f:
    for sor in f:
        jelek.append( Jel(sor.strip().split(' ')) )

# 2.
print("2. feladat")
prompt:int = 3#int(input("Adja meg a jel sorszámát! ").strip())
prompt -= 1
print(f"x={jelek[prompt].x} y={jelek[prompt].y}")

# 3.
def eltelt(jel1:Jel, jel2:Jel)->int:
    return jel1.get_mp() - jel2.get_mp() # direkt lehet negativ

# 4.
print("\n4. feladat")
print( ido_format( eltelt(jelek[-1], jelek[0])) )