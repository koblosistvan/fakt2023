forrás = open("forgalom.txt", mode="r", encoding="utf-8")

időpont = []
áthaladás = []
irány = []

def idő_mp(óra, perc, mp):
    return óra*3600+perc*60+mp

forrás.readline()

for sor in forrás:
    adat = sor.strip().split(" ")
    időpont.append(idő_mp(int(adat[0]), int(adat[1]), int(adat[2])))
    áthaladás.append(int(adat[3]))
    irány.append(adat[4])

forrás.close()

print("2.feladat")
n = int(input("Mennyi az n értéke? "))
if irány[n-1] == "F":
    print("Alsóvárosba megy.")
else:
    print("Felsővárosba megy.")

print("3.feladat")
felső_felé = []
i = len(időpont)
while len(felső_felé) < 2:
    i -= 1
    if irány[i] == "A":
        felső_felé.append(időpont[i])

print(f'{felső_felé[0] - felső_felé[1]} mp különbséggel érte el az útszakaszt.')