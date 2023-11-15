import math
forrás = open('hajok.txt', mode='r', encoding='utf-8')
x = forrás.readline().strip()
konténer_db = int(x.split(' ')[0])
konténer_per_hajó = int(x.split(' ')[1])
városok = []
for i in forrás:
    városok.append(i.strip())
városok_id = list(set(városok))
kimenet = []
for i in range(len(városok_id)):
    if városok.count(városok_id[i]) % konténer_per_hajó != 0:
        csatolt = []
        csatolt.append(városok_id[i])
        csatolt.append(városok.count(városok_id[i]))
        kimenet.append(csatolt)
        csatolt = []
for i in range(3):
    if kimenet[i][1] / konténer_per_hajó == math.ceil(kimenet[i][1] / konténer_per_hajó):
        print(kimenet[i][0], kimenet[i][1] / konténer_per_hajó)
