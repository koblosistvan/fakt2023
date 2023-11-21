a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg egy másik számot: "))

if a >= b:
    if a % b == 0:
        print("Osztható")
elif b % a == 0:
    print("Osztható")
else:
    print("Nem osztható")











