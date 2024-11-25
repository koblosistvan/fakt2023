import random
forras=open('csapatnevek.txt',encoding='utf-8')

csapatok=[]
eredmenylista=[]

for sor in forras:
    adat=sor.strip().split('\n')
    csapatok.append(adat[0])

forras.close()
print(csapatok)

bekercsapat=input('Adj meg két csapatot kötőjellel elválasztva: ')
bekergol=input('Add meg a meccs eredményét kettősponttal elválasztva: ')


eredmenyek=bekergol.strip().split(':')
gol1=int(eredmenyek[0])
gol2=int(eredmenyek[1])

def x12(gol1,gol2):
    if gol1 > gol2:
        return '1'
    elif gol2 > gol1:
        return '2'
    else:
        return 'x'


csapatok_masolat=csapatok.copy()
meccsek=[]
for i in range(7):
    hazai = random.choice(csapatok_masolat)
    csapatok_masolat.remove(hazai)
    hazai_gol=random.randint(0,5)

    vendeg = random.choice(csapatok_masolat)
    csapatok_masolat.remove(vendeg)
    vendeg_gol = random.randint(0, 5)

    meccsek.append([hazai,hazai_gol,vendeg, vendeg_gol])

print('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény: ')

for meccs in meccsek:
    print(f"{meccs[0]} - {meccs[2]} {meccs[1]}:{meccs[3]} {x12(meccs[1], meccs[3])}")


ujforras=open('szelveny.txt', mode='w', encoding='utf-8')

print('Gergelyiugornyai totó, 53. hét, telitalálatos szelvény: ',file=ujforras)

megegy=1

for meccs in meccsek:
    print(f'{megegy}, {meccs[0]} - {meccs[2]} {meccs[1]}:{meccs[3]} {x12(meccs[1], meccs[3])}',file=ujforras)
    megegy +=1
print(eredmenyek)






