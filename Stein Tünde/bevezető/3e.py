p = 1
n = 3
m = 5
for n in range(3, 10000000, 4):
        p -= 1/n
for m in range(5, 10000000, 4):
        p += 1/m
p = p*4
print(f'π = {p}')