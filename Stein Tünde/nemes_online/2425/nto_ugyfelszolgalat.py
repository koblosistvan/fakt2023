elso_sor = input().split(' ')
n = elso_sor[0]
k = elso_sor[1]
masodik_sor = input().split(' ')
a = []
for i in masodik_sor:
    a.append(i)
dolgozok = 1
for i in range(len(a)-1):
    for z in range(0, i):
        plusz = True
        if a[z]+k <= a[i+1]:
            plusz = False
        if plusz:
            dolgozok += 1
            break
print(dolgozok)