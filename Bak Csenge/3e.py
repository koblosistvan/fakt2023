Pí = 1
a = 3


for i in range(1, 1000000):
    if i % 2 != 0:
        Pí -= (1 / a)
    else:
        Pí += (1 / a)
    a += 2

print(Pí, end="\n\n")

while a < 1000000:
    Pí += (1 / a)
    a += 2
    Pí -= (1 / a)
    a += 2

print(Pí, end="\n\n")
print(f"A Pí: {Pí * 4}")









