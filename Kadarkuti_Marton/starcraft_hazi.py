class Starcraft:
    def __init__(self, *args):
        self.name, self.cast, self.df, self.hp, self.melee, self.range = args
        
    def get(self):
        return list(map(str,[self.name, self.cast, self.df, self.hp, self.melee, self.range]))

data = []
with open("Kadarkuti_Marton\\starcraft.txt","r",encoding="utf-8") as f:
    f.readline()
    for sor in f:
        temp = sor.strip().split("\t")
        data.append(Starcraft(temp[0], temp[1], int(temp[2]), int(temp[3]), int(temp[4]), int(temp[5])))
        
print("1. feladat")
print(len(data), " egység adatait tartalmazza az állomány.\n")

print("2. feladat")
magas_index = [i.melee+i.range for i in data]
magas_index = magas_index.index(max(magas_index))
print("A legerősebb egység ",data[magas_index].name, data[magas_index].cast, " és ", data[magas_index].hp, " HP-ja van.\n")

print("3. feladat")
print(f'{len([i.melee for i in data if (i.melee >0)])} egység tud földi célpontokat támadni.\n')

print("4. feladat")
fdata = [i for i in data if (i.melee>0 and i.range >0)]
with open("Kadarkuti_Marton\\starcraft-tamadok.txt","w",encoding="utf-8") as x:
    for i in range(len(fdata)):
        x.write(" ".join(fdata[i].get()))
        x.write("\n")
print("starcraft-tamadok.txt sikeresen létrehozva.\n")

print("5. feladat")
zergek = [j for j in data if (j.cast == "Zerg" and j.melee>100 and j.range>100)]
if len(zergek)>0:
    print("Van ilyen Zerg egység.")
else:
    print("Nincs ilyen Zerg egység.")
print("")

print("6. feladat")
atlag_terran = [i.hp for i in data if (i.cast == "Terran")]
atlag_terran = sum(atlag_terran)/len(atlag_terran)
print(f"Az átlagos Terran egység {int(atlag_terran)} HP-val rendelkezik.\n")