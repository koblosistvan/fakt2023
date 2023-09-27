forrás = open('4c-bolt.txt', mode='r', encoding='utf-8')

bevétel = []
kiadás = []
for sor in forrás:
    adat = sor.strip().split(',')
    bevétel.append(int(adat[0]))
    kiadás.append((int(adat[1])))
forrás.close()

print(bevétel)
print(kiadás)

sok_bevétel = 0
veszteséges_napok = 0
nagyobb_profit = 0
for i in range(len(bevétel)):
    if bevétel[i] > kiadás[i] * 1.1:
        sok_bevétel += 1
    elif bevétel[i] < kiadás[i]:
        veszteséges_napok += 1
print(f'{sok_bevétel} napon volt több a bevétel a kiadásnál.')
print(f'{veszteséges_napok} veszteséges nap volt.')
for i in range(len(bevétel-1)):
     if bevétel[i] < bevétel[i+1]:
         nagyobb_profit +=1
print(f'{nagyobb_profit} napon volt több profit az előző naphoz képest.')