forrás = open('6b-forgalom.txt', mode='r')
a = forrás.readline().strip().split(' ')
hely_db = int(a[0])
adatok = int(a[1])
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
ip = óra * 60 + perc
if ip in időpont:
    print('Volt mérési eredmény ebben az időpontban.')
else:
    print('Nem volt mérési eredmény ebben az időpontban.')

for i in range(len(hely)):
    if időpont.count(i) >= 2:
        print('Volt olyan időpont, amikor két mérés volt.')
        break

hely.sort()
helyek = list(set(hely))
állomás = []
for i in range(hely_db):
    állomás.append(hely.count(i))
index = állomás.index(max(állomás))
print(állomás)
print(helyek[index])
