k = int(input('> '))
n = int(input('> '))
x = input().split(', ')
for i in range(len(x)):
    x[i] = int(x[i])
d=0
i = 1
M = 0
while i<=n and d<k:
    if x[i] % 2 == 0:
        d += 1
        if d == 1:
            j = i
    if d<k:
        i += 1
if d==k:
    M = i-j+1
a=j
b=i
while i<=n:
    i=i+1
    while i≤n és x[i] % 2 !=
 i:=i+1
 Ciklus vége
 j:=j+1
 Ciklus amíg X[j] nem páros
 j:=j+1
 Ciklus vége
 Ha i-j+1>M és i≤N akkor M:=i-j+1; A:=j; B:=i
 Ciklus vége
Elágazás vége