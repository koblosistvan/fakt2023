elso_sor = input().split(' ')
n = int(elso_sor[0])
k = int(elso_sor[1])
masodik_sor = input().split(' ')
a = []
for i in masodik_sor:
    a.append(int(i))
dolgozok = 1
for i in range(len(a)):
    plusz = True
    for z in range(i):
        b = a[z]
        c = a[i]
        if a[z]+k <= a[i]:
            plusz = False
            break
        if plusz:
            dolgozok += 1
print(dolgozok)

"""
3 2
1 2 3

4 1
1 1 2 3

3 3
1 2 3
"""