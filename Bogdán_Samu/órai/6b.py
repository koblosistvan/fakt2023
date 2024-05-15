forrás = open("Bogdán_Samu\órai\\6b-forgalom.txt", mode='r', encoding='utf-8')
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

leghosszabb_idő = max([időpont[i+1] - időpont[i] for i in range(len(időpont) - 1)])

print(leghosszabb_idő)
print(hely.count(50))

hatelott50 = len([i for i in range(len(hely)) if hely[i] == 50 and időpont[i] // 60 < 6])
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

stat = open('6b-statisztika.txt', mode='w', encoding='utf-8')
hely.sort()
helyek = list(set(hely))
for i in range(hely_db):
    stat.write(f'Állomás: {helyek[i]}, mérések: {hely.count(i+1)}')
    stat.write('\n')
stat.close()

állomás = []
for i in range(1, hely_db):
    állomás.append(hely.count(i))
index = állomás.index(max(állomás))
print(helyek[index])
