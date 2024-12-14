# Nemes Tihamér Online 2. forduló - 4. feladat - Puska
# Kadarkuti Márton

DEBUG_ELSO = "4 1"
DEBUG_SOROK = [
    "1 2",
    "1 5",
    "1 3",
    "1 7",
]

class Keplet:
    def __init__(self,data)->None:
        self.sorok = int(data[0])
        self.fontos = int(data[1])
    def __str__(self)->str:
        return str(self.sorok) + ' ' + str(self.fontos)

tmp = "" # seged
tmp = DEBUG_ELSO#input()
tmp = tmp.strip().split(' ')

kepletek_szama:int = int(tmp[0])
sorok_szama:int = int(tmp[1])
kepletek:list[Keplet] = []

for sor in range(kepletek_szama):
    tmp = DEBUG_SOROK[sor]#input()
    kepletek.append(Keplet(tmp.strip().split(' ')))

for i in kepletek:
    print(i)