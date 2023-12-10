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

árak = open('árak.txt', mode='w', encoding='utf-8')
for i in range(lakás_db):
    if 50 <= terület[i] <= 60:
        árak.write(f'terület: {terület[i]} m^2, ár: {ár[i]} millió Ft')
        árak.write('\n')
árak.close()

tart = str(input('Adjon meg egy ártartományt milliókban, "min-max" formátumban: '))
minimum = int(tart.strip().split('-')[0])
maximum = int(tart.strip().split('-')[1])

for i in range(lakás_db):
    if minimum <= ár[i] <= maximum:
        print(f'Ingatlan száma: {ár.index(ár[i])}, alapterület: {terület[i]}, ár: {ár[i]}.')
else:
    print('Ebben az ártartományban nincsen ingatlan.')

ter_ar = str(input('Adjon meg egy alapterületet m^2-ben és egy árat milliókban, "terület-ár" formátumban: '))
ter = int(ter_ar.strip().split('-')[0])
ar = int(ter_ar.strip().split('-')[1])
ingatlan = []
for i in range(lakás_db):
    if terület[i] == ter and ár[i] == ar:
        ingatlan.append(int(ár.index(ár[i])) + 1)
if len(ingatlan) > 0:
    print(f'Ingatlan(ok) sorszáma: {ingatlan}')
else:
    print('Nincs a megadott adatoknak megfelelő ingatlan.')
