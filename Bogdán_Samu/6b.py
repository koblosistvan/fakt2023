forrás = open('6b-forgalom.txt', mode='r')
a = forrás.readline().strip().split(' ')
hely_db = a[0]
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

óraperc = str(input('Adjon meg egy időpontot "óra:perc" formátumban! '))
óra = int(óraperc.split(':')[0])
perc = int(óraperc.split(':')[1])

if (óra * 60 + perc) in időpont:
    print('Volt mérési eredmény ebben az időpontban.')
else:
    print('Nem volt mérési eredmény ebben az időpontban.')
