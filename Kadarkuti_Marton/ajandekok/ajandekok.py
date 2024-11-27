
KULONBOZO_AJANDEKOK_SZAMA:int = 0

class Doboz:
    INSTANCEK_SZAMA = 0
    OSSZES_DARAB:int = 0
    MAX_DARAB:int = 0
    ATLAG_DARAB:int = 0

    def __init__(self, data:list)->None:
        Doboz.INSTANCEK_SZAMA += 1
        self.id = Doboz.INSTANCEK_SZAMA # sorszam

        self.data_str = data[1:]
        data = list(map(int, data))
        self.darab = data[0]
        self.data = data[1:]

        Doboz.OSSZES_DARAB += self.darab
        if Doboz.MAX_DARAB < self.darab:
            Doboz.MAX_DARAB = self.darab
    
    def get_str(self)->str:
        return f"{self.darab}db: {' '.join(self.data_str)}"

    def __str__(self)->str:
        return self.get_str()

# 1. feladat
dobozok:list[Doboz] = []
with open("Kadarkuti_Marton\\ajandekok\\dobozok.txt",'r',encoding="utf-8") as f:
    KULONBOZO_AJANDEKOK_SZAMA = int(f.readline().split(' ')[1]) # 15

    for sor in f:
        dobozok.append( Doboz(sor.strip().split(' ')) )

"""A játékokat egyenletesen el lehet osztani a dobozokban."""

# 2. feladat
Doboz.ATLAG_DARAB = int( Doboz.OSSZES_DARAB/len(dobozok) )

if not Doboz.OSSZES_DARAB % len(dobozok):
    print("A játékokat egyenletesen el lehet osztani a dobozokban.")
else:
    print("A játékokat nem lehet egyenletesen elosztani a dobozokban.")
print("Játékok dobozonkénti átlagos száma:", Doboz.ATLAG_DARAB)

# 3. feladat
print("Legtöbb játék egy dobozban (",Doboz.MAX_DARAB, " db) a következő dobozokban volt: ",' '.join([str(i+1) for i in range(len(dobozok)) if dobozok[i].darab==Doboz.MAX_DARAB]),sep='')

# 4. feladat
statisztika = [0]*KULONBOZO_AJANDEKOK_SZAMA
for doboz in dobozok:
    for i in doboz.data:
        statisztika[i-1] += 1

nepszeru_indexek = []
for i in range(KULONBOZO_AJANDEKOK_SZAMA):
    if statisztika[i] == max(statisztika):
        nepszeru_indexek.append(str(i+1))

print("Legnépszerűbb játék(ok):",' '.join(nepszeru_indexek))

#5. feladat
print("Melyik dobozokból kell elvenni:")
for doboz in dobozok:
    if doboz.darab > Doboz.ATLAG_DARAB:
        print(f"{doboz.id}. dobozból {doboz.darab - Doboz.ATLAG_DARAB} db játékot")

# 6. feladat
berakhato_txt = open("Kadarkuti_Marton\\ajandekok\\berakhato.txt",'w',encoding="utf-8")
print("A hiányos dobozokba melyik játék rakható:")

temp:list[int] = [] # adott dobozba melyikek rakhatok
for doboz in dobozok:
    if doboz.darab < Doboz.ATLAG_DARAB:
        for i in range(1,1+KULONBOZO_AJANDEKOK_SZAMA):
            if i not in doboz.data:
                temp.append(str(i))
        temp = f"{doboz.id}. doboz: {' '.join(temp)}"
        print(temp)
        berakhato_txt.write(temp + '\n')
    temp = []

berakhato_txt.close()