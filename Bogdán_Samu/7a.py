forrás = open('7a-lakas-arak.txt', mode='r')
lakás_db = int(forrás.readline())
terület = []
ár = []

for i in forrás:
    sor = i.strip().split(' ')
    terület.append(int(sor[0]))
    ár.append(int(sor[1]))
forrás.close()
print(f'{ár.index(max(ár))}. lakás, {max(ár)} millió Ft.')

for i in range(lakás_db):
    if ár[i] >= 500:
        print('Van 500 millió Ft-nál drágább lakás.')
        break
else:
    print('Nincs 500 millió Ft-nál drágább lakás.')

nm_ár = []
for i in range(lakás_db):
    nm_ár.append(ár[i] / terület[i])
print(f'A(z) {nm_ár.index(max(nm_ár)) + 1}. lakásnak van a legmagasabb négyzetméter ára.')

husz = 0
for i in range(lakás_db):
    if ár[i] <= 20:
        husz += 1
print(f'{husz} darab 20 millió Ft alatti ingatlan van.')
