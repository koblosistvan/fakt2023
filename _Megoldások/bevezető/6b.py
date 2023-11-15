forrás = open('6b-forgalom.txt', mode='r', encoding='utf-8')

hely = []
időpont = []

forrás.readline()
for sor in forrás:
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    időpont.append(int(adat[1])*60 + int(adat[2]))
forrás.close()

# bőbeszédű verzió
def óra_perc(i):
    időérték = időpont[i]
    óra = időérték // 60
    perc = időérték % 60
    return f'{óra:0>2d}:{perc:0>2d}'

# tömörebb verzió
def óra_perc2(i):
    return f'{időpont[i]//60}:{időpont[i]/60}'

# 1. feladat
print('-' * 30)
leghosszabb_id = 0
leghosszabb_idő = időpont[1] - időpont[0]
for i in range(len(hely)-1):
    if időpont[i+1] - időpont[i] > leghosszabb_idő:
        leghosszabb_id = i
        leghosszabb_idő = időpont[i+1] - időpont[i]

print(f'A leghosszabb szünet {leghosszabb_idő} perc volt {óra_perc(leghosszabb_id)} és {óra_perc(leghosszabb_id+1)} között.')
print('Vége.')

# darabszámok
állomás_db = [0] * 100
for i in range(len(hely)):
    állomás_db[hely[i]-1] += 1
