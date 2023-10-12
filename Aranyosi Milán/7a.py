kimenet = open('arak.txt', mode='w', encoding='utf8')

print(f'Eddig is írtunk ilyet.', file=kimenet)

kimenet.close()

forras = open('7a-lakas-arak.txt', mode='r', encoding='utf8')
meret = []
ar = []

forras.readline()
for sor in forras:
    adat = sor.strip().split(' ')
    meret.append(int(adat[0]))
    ar.append(int(adat[1]))
forras.close()
print(ar)
print(meret)

legdragabb = ar[0]
legdragabb_id = 0
for i in range(len(ar)):
    if ar[i] > legdragabb:
        legdragabb = ar[i]
        legdragabb_id = i
print(f'A legdragabb ház {legdragabb} millió forintba kerül, {legdragabb_id} a sorszáma.')

for i in range(len(ar)):
    if ar[i] > 500:
        print('Van 500 milliónál drágább ház.')
        break
else:
     print('Nincs 500M forintnál dgágább ház.')

