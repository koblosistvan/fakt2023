class starcraft:
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
    mindenegyseg.append(starcraft(egyseg=str(adat[0]), faj=str(adat[1]), pajzs=int(adat[2]), hp=int(adat[3]), foldellen=int(adat[4]), levegoellen=int(adat[5])))
forras.close()

#1. feladat

print(len(mindenegyseg),'egyseget tartalmaz')

# 3. feladat

protossokfold = 0

for i in range(len(mindenegyseg)):
    if

