import math
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
        megnezte.append(int(adat))
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
    if megnezte[i]==1:
        latta+=1
    else:
        nemlatta+=1


print(latta, nemlatta)

szazalek=latta/len(megnezte)*100
print(f'{szazalek:.2f} százalékát látta')


#3
nezettpercek=[]

for i in range(len(megnezte)):
    if megnezte[i]==1:
        nezettpercek.append(hossz[i])


osszesnezettperc=sum(nezettpercek)
print(osszesnezettperc)
napok=osszesnezettperc/1440
napvissza=(int(napok))*1440
oravissza=int(napok)*24
orak=(osszesnezettperc/60)-oravissza
percek=osszesnezettperc-napvissza-int(orak)*60
print(f'{(math.floor(napok))} nap, {(math.floor(orak))} óra,  {(math.floor(percek))} percet')



#4

beker=(input('Add meg a kért dátumot(éééé.hh.nn): '))
for i in range(len(adasdate)):
    if adasdate[i] <= beker and megnezte[i] == 0:
        print(f'{evadresz[i], cim[i]}')


#5


def hetnap(ev, ho, nap)
 napok= (″v″, ″h″, ″k″, ″sze″,″cs″, ″p″, ″szo″)
 honapok= (0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4)
 if ho < 3:
     ev=ev-1
 hetnapja = napok[(ev + ev div 4 – ev div 100 + v div 400 + honapok[ho-1] + nap) mod 7]



