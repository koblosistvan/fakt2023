import random
a = random.randint(0,999)
b = random.randint(0,999)

input = input("Szám: ")

c = a + b
print(c)

if input == c:
    print("Jo")
else:
    print("Nem jo")