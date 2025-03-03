forras = open('rendel.txt', mode='r', encoding='utf-8')


nap=[]
varos=[]
darab=[]


for sor in forras:
    adat=sor.strip().split(' ')
    nap.append(adat[0])
    varos.append(adat[1])
    darab.append(int(adat[2]))

forras.close()

#2.f

print(f'{len(darab)} darab rendelést adtak le')

#3.f

beker=(input('Add meg a nap számát: '))

osszead=0
for i in range(len(nap)):
    if nap[i] == beker:
         osszead += darab[i]
print(f'{osszead} darab rendelést adtak le az adott napon')


legtobb=max(darab)

print(f'a legtobb rendeles {legtobb} volt és  napon adták le')


