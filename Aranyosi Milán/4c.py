forras = open('4c-bolt.txt', mode='r', encoding='utf-8')

bevétel = []
kiadás = []
for sor in forras:
    adat = sor.strip().split(',')
    bevétel.append(int(adat[0]))
    kiadás.append(int(adat[1]))
forras.close()

vesztegseg = 0
for i in range(len(bevétel)):
    if bevétel[i] < kiadás[i]:
        vesztegseg += 1
print(f'{vesztegseg} nap volt veszteséges.')

sokbevetel = 0
for i in range(len(bevétel)):
    if bevétel[i] > kiadás[i] * 1.1:
        sokbevetel += 1
print(f'{sokbevetel} napon volt több.')

osszeg = 0
for i in range(len(bevétel)):
    osszeg += bevétel[i] - kiadás[i]
print(f'Teljes profit: {osszeg : ,}')

hetv_osszeg = 0
for i in range(len(bevétel)):
    if i % 7 in (5 , 6):
        hetv_osszeg += bevétel[i] - kiadás[i]
        print(f'Hétvégi profit: {hetv_osszeg}')

