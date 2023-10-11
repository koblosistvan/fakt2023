forrás = open('6b-forgalom.txt', mode='r')
a = forrás.readline().strip().split(' ')
helyek = a[0]
adatok = a[1]
hely = []
időpont = []

for i in forrás:
    adat = i.strip().split(' ')
    hely.append(int(adat[0]))
    időpont.append(int(adat[1])*60 + int(adat[2]))
forrás.close()


leghosszabb_id = 0
leghosszabb_idő = időpont[1] - időpont[0]
for i in range(len(hely)-1):
    if időpont[i+1] - időpont[i] > leghosszabb_idő:
        leghosszabb_id = i
        leghosszabb_idő = időpont[i+1] - időpont[i]
print(hely.count(50))
hatelott50 = 0
for i in range(len(hely)):
    if hely[i] == 50 and (időpont[i] // 60 < 6):
        hatelott50 += 1
print(hatelott50)

bekert_idopont = input('Adj meg egy időpontot:').split(':')
bekert_idoertek = int(bekert_idopont[0]) * 60 + int(bekert_idopont[1])
for i in range(len(hely)):
     if bekert_idoertek == időpont[i]:
         print('Van a megadott időpontban mérés.')
         break
else:
    print('Nincs a megadott időpontban mérés.')


adott_időpont = időpont[i]
for i in range(len(hely)):
    if időpont[i] == len(időpont) - időpont[i]:
        print('Volt olyan időpont.')
        break
else:
    print('Nem volt olyan időpont.')
