forras=open('dobozok.txt', encoding='utf-8')

dobozok=[]
ajandekdarab=[]

forras.readline()
for sor in forras:
    adat=sor.strip().split(' ')
    ajandekdarab.append(int(adat[0]))
    dobozok.append(sor.strip().split(' '))

forras.close()

atlag=sum(ajandekdarab)//len(ajandekdarab)
print(f'Játékok dobozonkénti átlagos száma: {atlag}')

if sum(ajandekdarab)%atlag==0:
    print('A játékokat egyenletesen el lehet osztani a dobozokban.')
else:
    print('Nem lehet')


for i in range(len(dobozok)):
    szamldoboz = 0
    legtobb=max(dobozok[i])
    if legtobb==ajandekdarab[i]:




print(f'Legtöbb játék egy dobozban: {legtobb} a {szamldoboz} ')


tobb=max(dobozok)
