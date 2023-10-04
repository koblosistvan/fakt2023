import random

hőmérsékletek = []
összeg = 0
csökkenés = 0
növekedés = 0
legkisebb = 100
legnagyobb = 0

nagyobb_30 = 0
for i in range(46):
    hőmérsékletek.append(random.randint(15, 35))
for i in range(len(hőmérsékletek)):
    if hőmérsékletek[i] > 30:
        nagyobb_30 += 1
    összeg += hőmérsékletek[i]
    if hőmérsékletek[i] < legkisebb:    #:c
        legkisebb = hőmérsékletek[i]
    if hőmérsékletek[i] > legnagyobb:
        legnagyobb = hőmérsékletek[i]

for i in range(len(hőmérsékletek)-1):
    if hőmérsékletek[i] > hőmérsékletek[i+1]:
        csökkenés += 1
    elif hőmérsékletek[i] < hőmérsékletek[i+1]:
        növekedés += 1


print(f'Beolvastam {len(hőmérsékletek)} rekordot.\n{nagyobb_30} alkalommal mértünk 30°C-nál többet.\nAz átlaghőmérséklet: {összeg/len(hőmérsékletek)}°C')
print(f'{növekedés} alkalommal nőtt, és {csökkenés} alkalommal csökkent a hőmérséklet az előző méréshez képest.')
print(f'A legmagasabb mért hőmérséklet {legnagyobb}°C, a legalacsonyabb mért hőmérséklet {legkisebb}°C volt.')
