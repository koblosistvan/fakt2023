import random

bekértnevek = input('Adja meg két csapat nevét, egy sorban, pontosan egy kötőjellel elválasztva a két nevet! : ')
bekérteredmény = input('Adja meg a két csapat által játszott meccs eredményét is, a rúgott gólok számait pontosan egy kettősponttal elválasztva! : ')
print('\n')
def x12(gól1, gól2,):
   if int(gól1) > int(gól2):
      return '1'
   elif int(gól2) > int(gól1):
      return '2'
   else:
      return 'X'

forras = open("PigaiPéter\\csapatnevek.txt", mode='r', encoding='utf-8')
csapatnevek = []
for sor in forras:
   nev = sor.strip().split('\n')
   csapatnevek.append(nev[0])
forras.close()

megvolt = []
merkozesek = []
pontszamok1 = []
pontszamok2 = []
csapat1 = []
csapat2 = []
while len(csapatnevek) > 0:
    hazai = random.choice(csapatnevek)
    csapat1.append(hazai)
    megvolt.append(csapatnevek.pop(csapatnevek.index(hazai)))

    vendég = random.choice(csapatnevek)
    csapat2.append(vendég)
    megvolt.append(csapatnevek.pop(csapatnevek.index(vendég)))

    eredmeny1 = random.randint(0,5)
    pontszamok1.append(eredmeny1)
    eredmeny2 = random.randint(0,5)
    pontszamok2.append(eredmeny2)

    merkozesek.append(f'{hazai} - {vendég} {eredmeny1}:{eredmeny2} {x12(eredmeny1, eredmeny2)}')
megvolt,csapatnevek = csapatnevek, megvolt

bekértnevek = bekértnevek.split('-')
bekérteredmény = bekérteredmény.split(':')

pontszamok1.append(int(bekérteredmény[0]))
pontszamok2.append(int(bekérteredmény[1]))
csapat1.append(bekértnevek[0])
csapat2.append(bekértnevek[1])

gólkülönb = abs(pontszamok1[0]-pontszamok2[0])
for i in range(len(pontszamok1)):
   if abs(pontszamok1[i]-pontszamok2[i]) > gólkülönb:
      gólkülönb = abs(pontszamok1[i]-pontszamok2[i])
gólkülönblista = []
for i in range(len(pontszamok1)):
   if abs(pontszamok1[i]-pontszamok2[i]) == gólkülönb:
      if i == len(pontszamok1)-1:
         gólkülönblista.append('+1')
      else:
         gólkülönblista.append(str(i+1))

dontetlen = []
for i in range(len(pontszamok1)):
   if pontszamok1[i] == 0 and pontszamok2[i] == 0:
      if i == len(pontszamok1)-1:
         dontetlen.append('+1')
      else:
         dontetlen.append(str(i+1))

kétgól = []
for i in range(len(pontszamok1)):
   if pontszamok1[i]-pontszamok2[i] >= 2:
      kétgól.append(csapat1[i])
   elif pontszamok2[i]-pontszamok1[i] >= 2:
      kétgól.append(csapat2[i])

print('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:')
print('\n'.join(merkozesek))
print(f'{bekértnevek[0]} - {bekértnevek[1]} {bekérteredmény[0]}:{bekérteredmény[1]} {x12(bekérteredmény[0], bekérteredmény[1])}')
print(f'\nLegnagyobb gólkülönbségű mérkőzések: {" ".join(gólkülönblista)}\n')
if len(dontetlen) > 0:
   print(f'0:0-ás mérkőzések: {" ".join(dontetlen)}\n')
print(f'Legalább két góllal nyertek: {" ,".join(kétgól)}')

szelveny = open('PigaiPéter\\szelveny.txt', mode='w', encoding='utf-8')
szelveny.write('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény:\n')
szelveny.write('\n'.join(merkozesek))
szelveny.write('\n')
szelveny.write(f'{bekértnevek[0]} - {bekértnevek[1]} {bekérteredmény[0]}:{bekérteredmény[1]} {x12(bekérteredmény[0], bekérteredmény[1])}\n')
szelveny.write(f'Legnagyobb gólkülönbségű mérkőzések: {" ".join(gólkülönblista)}')
if len(dontetlen) > 0:
   szelveny.write(f'0:0-ás mérkőzések: {" ".join(dontetlen)}')
szelveny.write(f'Legalább két góllal nyertek: {" ,".join(kétgól)}')