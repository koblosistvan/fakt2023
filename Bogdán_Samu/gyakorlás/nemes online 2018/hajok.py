import math
forrás = open('hajok.txt', mode='r', encoding='utf-8')
x = forrás.readline().strip()
konténer_db = int(x.split(' ')[0])
konténer_per_hajó = int(x.split(' ')[1])
városok = []
for i in forrás:
    városok.append(i.strip())
városok_id = list(set(városok))
városok_db = []
for i in range(len(városok_id)):
    városok_db.append(városok.count(városok_id[i]))
városok_db1 = városok_db
index = []
for i in range(3):
    index.append(városok_db.index(max(városok_db1)))
    városok_db[városok_db1.index(max(városok_db1))] = 0
for i in range(3):
    print(városok_id[index[i]])
