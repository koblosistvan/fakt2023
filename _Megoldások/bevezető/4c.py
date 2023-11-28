forrás = open('4c-bolt.txt', mode='r', encoding='utf-8')

bevétel = []
kiadás = []
for sor in forrás:
    adat = sor.strip().split(',')
    bevétel.append(int(adat[0]))
    kiadás.append(int(adat[1]))
forrás.close()

sok_bevétel_számláló = 0
for i in range(len(bevétel)):
    if bevétel[i] > kiadás[i] * 1.1:
        sok_bevétel_számláló += 1
print(f'{sok_bevétel_számláló} napon volt 10%-kal több a bevétel a kiadásnál.')

profit_összeg = 0
for i in range(len(bevétel)):
    profit_összeg += bevétel[i] - kiadás[i]
print(f'A teljes profit {profit_összeg:,} volt.')

hétvégi_profit_összeg = 0
for i in range(len(bevétel)):
    if i % 7 in (5, 6):
        hétvégi_profit_összeg += bevétel[i] - kiadás[i]
print(f'A hétvégi profit {hétvégi_profit_összeg:,} volt.')


