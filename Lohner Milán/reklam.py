forras =open('rendel.txt', mode='r', encoding='utf-8')


nap=[]
varos=[]
darab=[]


for sor in forras:
    adat=sor.strip().split(' ')
    nap.append(adat[0])
    varos.append(adat[1])
    darab.append(adat[2])

forras.close()

#2.f

print(f'{len(darab)} darab rendelést adtak le')

#3.f

beker=int(input('Add meg a nap számát: '))

for i in range(len(nap)):
    elso=nap[i]==1
