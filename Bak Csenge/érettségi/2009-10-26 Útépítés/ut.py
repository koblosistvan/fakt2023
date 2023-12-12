időpont = []
áthaladás = []
irány = []
óra = []

def idő(ó, p, mp):
    return ó*3600 + p*60 + mp

forrás = open("forgalom.txt", mode="r", encoding="utf-8")

első_sor = forrás.readline()

for sor in forrás:
    adat = sor.strip().split(" ")
    időpont.append(idő(int(adat[0]), int(adat[1]), int(adat[2])))
    áthaladás.append(int(adat[3]))
    irány.append(adat[4])
    óra.append(adat[0])

forrás.close()


bekért = int(input("Adj meg egy számot "))

n_irány = "Also város" if irány[bekért-1] == "F" else "Felső város"
print(n_irány)

felső_felé = []
i = len(irány)

while len(felső_felé) < 2:
    i -= 1
    if irány[i] == "F":
        felső_felé.append(időpont[i])

print(abs(felső_felé[0]-felső_felé[1]))

kiszámolt_Alsó = 0
kiszámolt_Felső = 0


for i in range(len(óra)-1):
    if óra[i] == óra[i+1]:
        if irány[i] == "A":
            kiszámolt_Alsó += 1
        if irány[i] == "F":
            kiszámolt_Felső += 1

    if óra[i] != óra[i+1] or i+2 == len(óra):
        if irány[i] == "A":
            kiszámolt_Alsó += 1
        if irány[i] == "F":
            kiszámolt_Felső += 1
        print(óra[i - 1], kiszámolt_Alsó, kiszámolt_Felső)
        kiszámolt_Alsó = 0
        kiszámolt_Felső = 0
        if óra[i+1] == óra[-1] and i+1 == len(óra):
            if irány[i] == "A":
                kiszámolt_Alsó += 1
            if irány[i] == "F":
                kiszámolt_Felső += 1
            print(óra[i+1], kiszámolt_Alsó, kiszámolt_Felső)




















