forras = open('esos.txt', mode='r', encoding='utf-8')
forras.readline()
mm = list(map(int, forras.readline().strip().split(' ')))
volt = 0
for i in range(len(mm)):
    if mm[i] != 0:
        volt += 1
egyhuzamban = 0
leghoszabb = 0
for i in range(len(mm)-1):
    if mm[i] == 0 and mm[i + 1] == 0:
        egyhuzamban += 1
    if mm[i] == 0 and mm[i + 1] != 0:
        egyhuzamban += 1
        if egyhuzamban > leghoszabb:
            leghoszabb = egyhuzamban
            egyhuzamban = 0
print(f'{volt} napon esett az eső')
print(f'{leghoszabb} napig nem volt eső')
