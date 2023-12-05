import math
forrás = open('hajok.txt', mode='r', encoding='utf-8')

első_sor = forrás.readline().strip().split(' ')
össz_kont = int(első_sor[0])
kph = int(első_sor[1])

célállomások = []

for sor in forrás:
    célállomások.append(sor.strip())

forrás.close()

városok = set(célállomások)
hajók = []

for város in városok:
    konténer_városba = célállomások.count(város)
    hajó_városba = math.ceil(konténer_városba/kph)
    hajók.append([város, hajó_városba, hajó_városba*kph - konténer_városba])

for i in range(len(hajók)):
    for j in range(len(hajók)):
        if hajók[i][2] > hajók[j][2] or (hajók[i][2] == hajók[j][2] and hajók[i][1] > hajók[j][1]):
            hajók[i], hajók[j] = hajók[j], hajók[i]

for i in range(3):
    print(f'{hajók[i][0]} {hajók[i][1]} {hajók[i][2]}')

