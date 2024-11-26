dobozok = open('Bogdán_Samu\\órai\\dobozok.txt', 'r')
 
x = dobozok.readline()
doboz_db = int(x.strip().split(' ')[0])
ajándék_db = int(x.strip().split(' ')[1])
 
játék_db = []
játékok = []
játékok_össz = []
for i in dobozok:
    játék_db.append(int(i.strip().split(' ')[0]))
    sor = []
    for e in range(int(i.strip().split(' ')[0])):
        sor.append(int(i.strip().split(' ')[e + 1]))
        játékok_össz.append(int(i.strip().split(' ')[e + 1]))
    játékok.append(sor)
 
dobozok.close()
 
if sum(játék_db) % doboz_db == 0:
    print('A játékokat egyenletesen el lehet osztani a dobozokban.')
else:
    print('A játékokat nem lehet egyenletesen elosztani a dobozokban.')
 
print(f'Játékok dobozonkénti átlagos száma: {int(round(sum(játék_db) / len(játék_db), 0))}')
 
max_ind = []
for i in range(doboz_db):
    if játék_db[i] == max(játék_db):
        max_ind.append(i + 1)
 
print(f'Legtöbb játék egy dobozban ({max(játék_db)} db) a következő dobozokban volt: {" ".join(map(str, max_ind))}')
 
népszerű = []
for i in range(ajándék_db):
    népszerű.append(játékok_össz.count(i + 1))
 
népszerű_ind = []
for i in range(ajándék_db):
    if népszerű[i] == max(népszerű):
        népszerű_ind.append(i + 1)
 
print(f'Legnépszerűbb játék(ok): {" ".join(map(str, népszerű_ind))}')
 
for i in range(doboz_db):
    if játék_db[i] > int(round(sum(játék_db) / len(játék_db), 0)):
        print(f'{i + 1}. dobozból {játék_db[i] - int(round(sum(játék_db) / len(játék_db), 0))} db játékot')
 
print('A hiányos dobozokba melyik játék rakható:')

for i in range(doboz_db):
    hiány = []
    if játék_db[i] < int(round(sum(játék_db) / len(játék_db), 0)):
        for e in range(ajándék_db):
            if (e + 1) not in játékok[i]:
                hiány.append(e + 1)
        print(f'{i + 1}. doboz: {" ".join(map(str, hiány))}')
