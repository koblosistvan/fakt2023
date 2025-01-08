forras=open('szallit.txt', mode='r', encoding='utf-8')

oszlop1=[]
oszlop2=[]
oszlop3=[]
oszlop4=[]

forras.readline()

for sor in forras:
    adat=sor.strip().split(' ')
    oszlop1.append(int(adat[0]))
    oszlop2.append(int(adat[1]))
    oszlop3.append(int(adat[2]))
    oszlop4.append(int(adat[3]))

forras.close()


#2.feladat
for i in range(len(oszlop1)):
    beker = int(input('Add meg a szállítás sorszámát: '))-1
    print(f'{oszlop2[beker]} indulással {oszlop3[beker]} célhellyel')
#3.feladat
def tav(szalaghossz, indulashelye, erkezeshelye):
#keplet
