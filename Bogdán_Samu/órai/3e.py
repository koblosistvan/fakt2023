x = 1
y = 1

for i in range(1000000):
     x = x + 2
     y = y - (1 / x) + (1 / (x + 2))
     x = x + 2

pi = y * 4

print(f"Az összefüggés alapján pí = {pi}.")
