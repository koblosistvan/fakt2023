class Meres:
    def __init__(self, ora: int, perc, masodperc, idő, honnan: str):
        self.ora = ora
        self.perc = perc
        self.masodperc = masodperc
        self.idő = idő
        self.sebesseg = 1000/idő
        self.honnan = honnan
        self.honnan_str = "Felső" if honnan == "F" else "Alsó"
        self.hova = "Felsőváros" if honnan == "A" else "Alsó város"

    def ido_mp(self):
        return self.ora*3600 + self.perc*60 + self.masodperc

    def ido_str(self):
        return f"{self.ora}:{self.perc}:{self.masodperc}"

    def __gt__(self, other):
        if self.sebesseg > other.sebesseg:
            return True
        else:
            return False

    def kilep_mp(self):
        return self.ido_mp() + self.idő

    def kilep_str(self):
        ora = self.kilep_mp() // 3600
        perc = self.kilep_mp() % 3600 // 60
        masodperc = self.kilep_mp() % 60
        return f"{ora:0>2d}:{perc:0>2d}:{masodperc:0>2d}"
        return f"{ora:0>2d}:{perc:0>2d}:{masodperc:0>2d}"


forgalom = []
forras = open("forgalom.txt", mode="r", encoding="utf-8")
forras.readline()
for sor in forras:
    adat = sor.strip().split(" ")
    forgalom.append(Meres(int(adat[0]), int(adat[1]), int(adat[2]), int(adat[3]), str(adat[4])))
forras.close()

#n = int(input("Meyik jármű adatait kéred?"))
n=2
print(f"Az {n}. jármű { forgalom[n].hova } felé halad")


felso_fele = [meres for meres in forgalom if meres.honnan == "A"]
#print(f"Az utso ket auto kozott {felso_fele[-1].ido_mp()- felso_fele[-2].ido_mp}s telt el.")

for i in range(24):
    felso_felol = [meres for meres in forgalom if meres.honnan == "F" and meres.ora == i]
    also_felol = [meres for meres in forgalom if meres.honnan == "A" and meres.ora == i]
    if len(felso_felol) > 0 or len(also_felol) > 0:
        print(f"{i} {len(also_felol)} {len(felso_felol)}")

leggyorsabb = sorted(forgalom, reverse=True)
for i in range(10):
    print(f"{leggyorsabb[i].ido_str()} {leggyorsabb[i].honnan_str} {leggyorsabb[i].sebesseg}")

also_fele = [meres for meres in forgalom if meres.honnan == "F"]
idopont_mp = 0
idopont_str = ""
for i in range(len(also_fele)):
    if also_fele[i].kilep_mp() > idopont_mp:
        print(also_fele[i].kilep_str())
        idopont_mp = also_fele[i].kilep_mp()
        idopont_str = also_fele[i].kilep_str()
    else:
        print(idopont_str)










