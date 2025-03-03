n = int(input())
nevek = []
for i in range(n):
    bemenet = input()
    nevek.append(bemenet)
megfelelo = nevek.copy()
for i in range(len(nevek)):
    if len(nevek[i]) < 5:
        megfelelo.remove(nevek[i])
        continue
    for k in nevek[i]:
        if nevek[i].count(k) != 1:
            megfelelo.remove(nevek[i])
            break
nevek = megfelelo.copy()
if megfelelo:
    legrovidebb = len(megfelelo[0])
    for i in megfelelo:
        if len(i) < legrovidebb:
            legrovidebb = len(i)
    for i in nevek:
        if len(i) > legrovidebb:
            megfelelo.remove(i)
    megfelelo.sort()
if megfelelo:
    print(megfelelo[-1])
else:
    print('Nincs')
