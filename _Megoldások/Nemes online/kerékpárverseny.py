forrás = open('kerekparverseny.txt', mode='r', encoding='utf-8')
import random
első_sor = forrás.readline().strip().split(' ')
városok_száma = int(első_sor[0])
táv = int(első_sor[1])

szakasz_távok = []

for sor in forrás:
    szakasz_távok.append(int(sor.strip()))

forrás.close()

def jó_város(rajt):
    össz = 0
    cél = rajt
    while össz < 50 and cél < len(szakasz_távok)-1:
        cél += 1
        össz += szakasz_távok[cél-1]
    if össz == 50:
        return cél - rajt
    else:
        return 0

for i in range(len(szakasz_távok)):
    szakaszok = jó_város(i)
    if szakaszok > 0:
        print(f'{i+1}. városból {szakaszok} szakasszal megoldható a verseny.')


        print(a,)
        range()

        jó_város()

        random.randint(a=12, b=13)