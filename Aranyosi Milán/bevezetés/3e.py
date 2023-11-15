pi = 1
x = 3
for i in range(1, 100000000):
    if i % 2 == 0:
        pi += 1/x
    else:
        pi -= 1/x
    x += 2
pi = pi * 4
print(f'A pí értéke: {pi}')