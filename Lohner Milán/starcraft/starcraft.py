class Starcraft:
    def __init__(self, egyseg, faj, pajzs, hp, foldellen, levegoellen):
        self.egyseg=egyseg
        self.faj=faj
        self.pajzs=pajzs
        self.hp=hp
        self.foldellen=foldellen
        self.levegoellen=levegoellen


mindenegyseg=[]

forras=open('starcraft.txt')

forras.readline()


for sor in forras:
    adat=sor.strip().split('\t')
    mindenegyseg.append(Starcraft(egyseg=(adat[0]), faj=(adat[1]), pajzs=int(adat[2]), hp=int(adat[3]), foldellen=int(adat[4]), levegoellen=int(adat[5])))
forras.close()

#1. feladat

print(len(mindenegyseg),'egyseget tartalmaz')

#2. feladat

maxhp = mindenegyseg[0].hp
maxfaj = mindenegyseg[0].faj
maxnev = mindenegyseg[0].egyseg

print(f'A legtobb hp val: {maxfaj} rendelkezik, neve: {maxnev} hp ja {maxhp}.')


#3. feladat

szml = 0

for i in range(len(mindenegyseg)):
    if mindenegyseg[i].faj == 'Protoss' and mindenegyseg[i].foldellen > 0:
        szml +=1

print(f'{szml} olyan egysege van a protossoknak emely foldi celpontokat tud tamadni')

#4. feladat

txt = open('starcraft-tamadók.txt', mode='w', encoding='utf-8')

for i in range(len(mindenegyseg)):
    if mindenegyseg[i].foldellen > 0 and mindenegyseg[i].levegoellen > 0:
        print(f'{mindenegyseg[i].egyseg} {mindenegyseg[i].faj} {mindenegyseg[i].pajzs} {mindenegyseg[i].hp} {mindenegyseg[i].foldellen} {mindenegyseg[i].levegoellen}', file=txt)

txt.close()
#5. feladat

szml2 = 0
for i in range(len(mindenegyseg)):
    if mindenegyseg[i].faj =='Zerg' and mindenegyseg[i].foldellen > 100 or mindenegyseg[i].levegoellen >100:
      szml2 +=1
print(szml2,'olyan egyseg van')

#6.feladat

osszhp = 0
terranok = 0

for i in range(len(mindenegyseg)):
    if mindenegyseg[i].faj == 'Terran':
        osszhp += mindenegyseg[i].hp
        terranok += 1
print(f'A Terranok atlagos hpja: {osszhp // terranok}.')


