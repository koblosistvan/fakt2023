forrás = open("4c-bolt.txt", mode='r', encoding='utf-8')

bevétel = []
kiadás = []
for sor in forrás:
    adat = sor.strip().split(',')
    bevétel.append(int(adat[0]))
    kiadás.append(int(adat[1]))
forrás.close()

bevétel_10 = 0
bevétel_nőtt = 0
hétvége = 0

for i in range(len(bevétel)-1):
    if bevétel[i] > kiadás[i] * 1.1:
        bevétel_10 += 1

    if (bevétel[i+1] - kiadás[i+1]) > (bevétel[i] - kiadás[i]):
        bevétel_nőtt += 1

for i in range(len(bevétel)):
    if i % 7 == 5 or i % 7 == 6:
        hétvége += (bevétel[i] - kiadás[i])

print(f'{bevétel_10} napon volt 10%-kal több a bevétel a kiadásnál.')
print(f'{bevétel_nőtt} napon nőtt a profit az előző naphoz képest.')
if hétvége > 0:
    print(f'{hétvége:,} .- a nyereség a teljes időszakaszban.')
elif hétvége == 0:
    print(f'Nincsen nyereség a teljes időszakban.')
else:
    hétvége = -hétvége
    print(f'{hétvége:,} .- a veszteség a teljes időszakaszban.')