import random

a=random.randint(1,10)
b=random.randint(1,10)

#print(a+b)

xerxes = int(input("Tippeld meg az összeget!: "))

if xerxes == a+b:
    print("Ügyes vagy!")
else:
    print("A fene a bundádat!")