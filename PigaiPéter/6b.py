import cuccok
forrás = open('6b.txt', mode='r', encoding='utf8')
cuccok.vonal()

forrás = open('6b-forgalom.txt', mode='r', encoding='utf-8')

hely = []
időpont = []

forrás.readline()
for sor in forrás:
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    időpont.append(int(adat[1])*60 + int(adat[2]))
forrás.close()

def óra_perc(i):
    időérték = időpont[i]
    óra = időérték // 60
    perc = időérték % 60
    return f'{óra:0>2d}:{perc:0>2d}'

def óra_perc2(i):
    return f'{időpont[i]//60}:{időpont[i]/60}'

print('-' * 30)
leghosszabb_id = 0
leghosszabb_idő = időpont[1] - időpont[0]
for i in range(len(hely)-1):
    if időpont[i+1] - időpont[i] > leghosszabb_idő:
        leghosszabb_id = i
        leghosszabb_idő = időpont[i+1] - időpont[i]

print(f'A leghosszabb szünet {leghosszabb_idő} perc volt {óra_perc(leghosszabb_id)} és {óra_perc(leghosszabb_id+1)} között.')
print('Vége.')

otvenes = 0

for i in range(len(hely)):
    if i == 50:
        otvenes += 1
print(f'{otvenes}szer van otvenes helyen meres')

bekert = int(input('adj meg egy idopontot'))
van = False
for i in range(len(idopont)):
    if i == bekert:
        van = True
if van:
    print('van ilyen idopont')
else:
    print('nincs ilyen idopont')

volt = False
for i in range(len(idopont)-1):
    if idopont[i] == idopont[i+1]:
        volt = True
if volt:
    print('volt azonos idopontban tobb meres')
else:
    print('nem volt azonos idopontban meres')
    


























