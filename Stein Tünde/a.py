kozelito = 1
n = int(input())
for i in range(2, n + 1, 1):
    kozelito = kozelito + 1 / ((i * 2 - 1) * (-1) ** n)
print(kozelito)
