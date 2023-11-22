import math
forrás = open('hajok.txt', mode='r', encoding='utf-8')
x = forrás.readline().strip().split(' ')
konténerek = int(x[0])
konténer_per_hajó = int(x[1])
városok = []
for sor in forrás:
    városok.append(sor.strip())
forrás.close()
város_id = list(set(városok))
város_id.sort()
hajók = []
for i in város_id:
    y = városok.count(i)
    hajók.append([i, math.ceil(y / konténer_per_hajó), y % konténer_per_hajó])
for i in range(len(hajók)):
    for e in range(len(hajók)):
        if hajók[i][2] > hajók[e][2] or (hajók[i][2] == hajók[e][2] and hajók[i][1] > hajók[e][1]):
            hajók[i], hajók[e] = hajók[e], hajók[i]
for i in range(3):
    print(hajók[i][0], hajók[i][1], hajók[i][2])
