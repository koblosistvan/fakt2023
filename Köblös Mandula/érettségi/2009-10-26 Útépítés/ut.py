forrás = open("forgalom.txt", mode="r", encoding="utf-8")

időpont = []
áthaladás = []
irány = []
óra = []
perc = []
másodperc = []

def idő_mp(óra, perc, mp):
    return óra*3600+perc*60+mp

forrás.readline()

for sor in forrás:
    adat = sor.strip().split(" ")
    időpont.append(idő_mp(int(adat[0]), int(adat[1]), int(adat[2])))
    áthaladás.append(int(adat[3]))
    irány.append(adat[4])
    óra.append(int(adat[0]))
    perc.append(int(adat[1]))
    másodperc.append(int(adat[2]))

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

print("4.feladat")
for e in range(24):
    felsőfelől = 0
    alsófelől = 0
    for i in range(len(időpont)):
        if óra[i] == e and irány[i] == "F":
            felsőfelől += 1
        elif óra[i] == e and irány[i] == "A":
            alsófelől += 1
    if felsőfelől > 0 or alsófelől > 0:
        print(e, alsófelől, felsőfelől)

print("5.feladat")
for i in range(len(időpont)-1):
    for e in range(len(időpont)-1):
        if áthaladás[e] > áthaladás[e+1]:
            áthaladás[e], áthaladás[e+1] = áthaladás[e+1], áthaladás[e]
            időpont[e], időpont[e+1] = időpont[e+1], időpont[e]
            irány[e], irány[e+1] = irány[e+1], irány[e]
            óra[e], óra[e+1] = óra[e+1], óra[e]

for i in range(10):
    print(f'{óra[i]}:{perc[i]}:{másodperc[i]} {"Felső" if irány[i] == "F" else "Alsó"}, {1000 / áthaladás[i]:.2f}')
