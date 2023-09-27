forrás = open("4c-bolt.txt", mode='r', encoding='utf-8')

bevétel = []
kiadás = []
for sor in forrás:
    adat = sor.strip().split(',')
    bevétel.append(int(adat[0]))
    kiadás.append(int(adat[1]))
forrás.close

bevétel_10 = 0
bevétel_nőtt = 0
hétvége = []

for i in range(len(bevétel)-1):
    if bevétel[i] > kiadás[i] * 1.1:
        bevétel_10 += 1

    if (bevétel[i+1] - kiadás[i+1]) > (bevétel[i] - kiadás[i]):
        bevétel_nőtt += 1

    if i % 6 == 0 or i % 7 == 0:
        if (bevétel[i] - kiadás[i]) > 0:
            hétvége.append(i)

print(f'{bevétel_10} napon volt 10%-kal több a bevétel a kiadásnál.')
print(f'{bevétel_nőtt} napon nőtt a profit az előző naphoz képest.')
print(f'')
