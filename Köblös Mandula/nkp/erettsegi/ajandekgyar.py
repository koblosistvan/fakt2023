forrás = open('dobozok.txt', mode='r', encoding='utf-8')

forrás.readline()

ajandekok_száma = []
ajandekok_az = []
for sor in forrás:
    adat = sor.strip().split(' ')
    ajandekok_száma.append(int(adat[0]))
    ajandekok_az.append([int(kód) for kód in adat[1:]])


forrás.close()

print(ajandekok_száma)
print(ajandekok_az)

atlag = sum(ajandekok_száma) / len(ajandekok_száma)
print(f'Játékok dobozonkénti átlagos száma: {atlag}')
if int(atlag) == atlag:
    print('A játékokat egyenletesen el lehet osztani a dobozokban.')
else:
    print('A játékokat egyenletesen nem lehet elosztani a dobozokban.')

legtobb = max(ajandekok_száma)
print(f'Legtöbb játék egy dobozban ({legtobb} db) a következő dobozokban volt:', end=' ')
for i in range(len(ajandekok_száma)):
    if legtobb == ajandekok_száma[i]:
        print(i+1, end=' ')

for i in range(len(ajandekok_az)):
    for j in range(len(ajandekok_az)-1):
        if ajandekok_az[j] in ajandekok_az[i+1]:
