rendel = open('Bogdán_Samu\\érettségi\\rendel.txt', 'r', encoding='utf-8')

nap = []
nap_alt = []
típus = []
típus_alt = []
darab = []
darab_alt = []

for i in rendel:
    x = i.strip().split(' ')
    nap.append(int(x[0]))
    nap_alt.append(int(x[0]))
    típus.append(x[1])
    típus_alt.append(x[1])
    darab.append(int(x[2]))
    darab_alt.append(int(x[2]))

rendel.close()

print('2. feladat:')
print(f'A rendelések száma: {sum(darab)}')

print('3. feladat:')
bekér = input('Kérem, adjon meg egy napot: ')

x = 0
for i in range(len(nap)):
    if nap[i] == bekér:
        x += darab[i]

print(f'A rendelések száma az adott napon: {x}')

print('4. feladat:')

