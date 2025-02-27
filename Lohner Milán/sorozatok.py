forras=open('lista.txt', mode='r', encoding='utf-8')

cim=[]
adasdate=[]
evadresz=[]
hossz=[]
megnezte=[]

i = 0
for sor in forras:
    adat = sor.strip()
    if i%5 == 0:
        adasdate.append(adat)
    if i%5 == 1:
        cim.append(adat)
    if i%5 == 2:
        evadresz.append(adat)
    if i%5 == 3:
        hossz.append(int(adat))
    if i%5 == 4:
        megnezte.append(adat)
    i += 1




nemismert = 0


for i in range(len(adasdate)):
    if 'NI' in adasdate[i]:
        nemismert += 1


vandatum=len(adasdate)-nemismert
print(f'{vandatum} dátummal rendelkező epizód van')


#2.
latta=0
nemlatta=0


for i in range(len(megnezte)):
    if '1' in megnezte[i]:
        latta+=1
    else:
        nemlatta+=1


print(latta, nemlatta)

szazalek=latta/len(megnezte)*100
print(f'{szazalek:.2f} százalékát látta')


#3
nezettpercek=[]

for i in range(len(megnezte)):
    if '1' in megnezte[i]:
        nezettpercek.append(hossz[i])


osszesnezettperc=sum(nezettpercek)
print(osszesnezettperc)
napok=osszesnezettperc/1440
print(f'{round(napok):.1f}')






