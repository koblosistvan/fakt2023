pontszam = int(input())
gy_pont = int(input())
d_pont = int(input())

gy = []
d = []
k = pontszam
max_n = k // d_pont + 1
for i in range(0, max_n):
    k = pontszam
    k -= d_pont*i
    d.append(i)
    gy.append(k // gy_pont)
    k -= (gy_pont)*(k // gy_pont)
    if k > 0:
        d[-1] += k//d_pont
        k -= d_pont*(k//d_pont)
    if len(gy) > 1 and len(d) > 1:
        if gy[-1] == gy[-2] and d[-1] == d[-2]:
            gy.remove(gy[-1])
            d.remove(d[-1])
for _ in range(len(gy)-1):
    for i in range(len(gy)-1):
        if gy[i] > gy[i+1]:
            gy[i], gy[i+1] = gy[i+1], gy[i]
            d[i], d[i + 1] = d[i + 1], d[i]
print(len(gy))
for i in range(len(gy)):
    print(f'{gy[i]} {d[i]}')

