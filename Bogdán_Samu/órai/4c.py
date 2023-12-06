forras = open('4c-bolt.txt', mode='r', encoding='utf-8')
bevetel = []
kiadas = []
for sor in forras:
    adat = sor.strip().split(',')
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))

forras.close()
print(bevetel)
print(kiadas)

bevetel_10 = 0
veszteseg = 0
profitnott = 0
wknd_profit = 0
for i in range(len(bevetel)):
    if bevetel[i] > (kiadas[i] * 1.1):
        bevetel_10 += 1
    if kiadas[i] > bevetel[i]:
        veszteseg += 1
    if i % 7 in (5, 6):
        wknd_profit += bevetel[i] - kiadas[i]
for i in range(len(bevetel) - 1):
    if (bevetel[i] - kiadas[i]) < (bevetel[i+1] - kiadas[i+1]):
        profitnott += 1
print(f'{veszteseg} veszteséges nap volt.')
print(f'{bevetel_10} olyan nap volt, amikor a bevétel legalább 10%-kal nagyobb volt a kiadásnál.')
print(f'{profitnott} olyan nap volt, amikor az előző naphoz képest nőtt a bolt profitja.')
print(f'Hétvégi profit: {wknd_profit:,}')
