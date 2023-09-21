forrás = open("4c-bolt.txt", mode="r", encoding="utf-8")

bevétel = []
kiadás = []

for sor in forrás:
    adat = sor.strip().split(",")
    bevétel.append(int(adat[0]))
    kiadás.append(int(adat[1]))

forrás.close()

vezsteség_napok = 0
sok_money = 0
nő_a_money = 0

for i in range(len(bevétel)):
    if bevétel[i] > kiadás[i] * 1.1:
        sok_money += 1
    if bevétel[i] < kiadás[i]:
        vezsteség_napok += 1
    if i != 0 and bevétel[i-1] - kiadás[i-1] < bevétel[i] - kiadás[i]:
        nő_a_money += 1


print(f"Nőtt a profit {nő_a_money} napon át")
print(f"A veszteséges napok száma: {vezsteség_napok}")
print(f"{sok_money} napon volt 10%-al több a bevétel a kiadásnál.")





