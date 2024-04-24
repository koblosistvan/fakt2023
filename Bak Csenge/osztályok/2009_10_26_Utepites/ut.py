class Meres:
    def __init__(self, ora: int, perc, masodperc, idő, honnan: str):
        self.ora = ora
        self.perc = perc
        self.masodperc = masodperc
        self.idő = idő
        self.sebesseg = 3600/idő
        self.honnan = honnan
        self.hova = "Felsőváros" if honnan == "A" else "Alsó város"

    def ido_mp(self):
        return self.ora*3600 + self.perc*60 + self.mp

forgalom = []
forras = open("forgalom.txt", mode="r", encoding="utf-8")
forras.readline()
for sor in forras:
    adat = sor.strip().split(" ")
    forgalom.append(Meres(int(adat[0]), int(adat[1]), int(adat[2]), int(adat[3]), str(adat[4])))
forras.close()

n = int(input("Meyik jármű adatait kéred?"))
print(f"Az {n}. jármű { forgalom[n].hova } felé halad")

print(f"Az utso ket auto kozott {forgalom[-1].ido_mp()- forgalom[-2].ido_mp}s telt el.")











