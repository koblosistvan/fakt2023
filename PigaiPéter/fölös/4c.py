forras = open('4c-bolt.txt', mode='r', encoding='utf-8')

bevétel = []
kiadás = []
for sor in forras:
    adat = sor.strip().split(',')
    bevétel.append(int(adat[0]))
    kiadás.append(int(adat[1]))
forras.close()
bevetelkeves = 0
bevételsok = 0
for i in range(len(bevétel)):
    if bevétel[i] > kiadás[i] * 1.1:
        bevételsok += 1
    else:
        bevetelkeves += 1
print(f'{bevételsok} napon volt több a bevétel a kiadásnál')
print(f'{bevetelkeves} napon volt kevesebb a bevétel a kiadásnál')
andor = 0
profitnagyobb = []
for i in range(len(bevétel)):
    profitnagyobb.append(bevétel[i] - kiadás[i])
    if profitnagyobb[i] < profitnagyobb[i - 1]:
        andor += 1
print(f'{andor} napon volt nagyobb a profit mint az előző nap')

profitosszeg = 0
for i in range(len(bevétel)):
    profitosszeg = bevétel[i] - kiadás[i]
print(f'{profitosszeg:,}')

hetvegiprofitossz = 0
for i in range(len(bevétel)):
    if i % 7 in (5,6):
        hetvegiprofitossz = bevétel[i] - kiadás[i]
print(f'{hetvegiprofitossz:,}')
