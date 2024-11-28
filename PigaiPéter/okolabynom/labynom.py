class Adatsor:
    evmax = 0
    evmin = 9999
    kapmax = 0
    kaporszag = ""
    gdpmin = 10**999
    gdpminorszag = ""
    def __init__(self,adatsor) -> None:
        self.eredeti = adatsor
        adatsor = adatsor.split(',')
        self.kód  = adatsor[0]
        self.ország = adatsor[1]
        self.régió = adatsor[2]
        self.év = int(adatsor[3])
        self.felhasználá = float(adatsor[4])
        self.kapacitá = float(adatsor[5])
        self.lakosság = adatsor[6]
        self.gdp = None if adatsor[7] == "None" else float(adatsor[7])
        if Adatsor.evmax < self.év:
            Adatsor.evmax = self.év
        if Adatsor.evmin > self.év:
            Adatsor.evmin = self.év
        if Adatsor.kapmax < self.kapacitá:
            Adatsor.kaporszag = self.ország
            Adatsor.kapmax = self.kapacitá
        if self.gdp != None and Adatsor.gdpmin > self.gdp:
            Adatsor.gdpmin = self.gdp
            Adatsor.gdpminorszag = self.orszag
    def __str__(self) -> str:
        return self.eredeti
adatok = []
with open("PigaiPéter\\okolabynom\\NFA light.csv", mode="r", encoding="utf-8") as forras:
    forras.readline()
    for sor in forras:
        adatok.append(Adatsor(sor.strip()))

print(f"{len(adatok)} sort tartalmaz")

print(f"{len([i for i in adatok if i.év == 2014])} országnak van 2014-es adata")

print(f"{Adatsor.evmin}-{Adatsor.evmax} közötti mérések")

print(f"A legnagyobb kapacitású ország {Adatsor.kaporszag} és {Adatsor.kapmax} a kapacitása")

print(f"Legkisebb gdp-vel rendelkező ország: {Adatsor.gdpminorszag}, {Adatsor.gdpmin}")
