print("-A program megadja, hogy két egész szám osztható-e egymással-")
a = int(input("Add meg az egyik [A] számot: "))
b = int(input("Add meg a másik [B] számot: "))

if a % b == 0:
    print(f"\nA osztható B-vel. \n   A/B = {int(a/b)}")
else:
    print(f"\nA nem osztható B-vel. \n   maradék: {a%b}")

if b % a == 0:
    print(f"\nB osztható A-val. \n   B/A = {b/a}")
else:
    print(f"\nB nem osztható A-val. \n   maradék: {int(b/a)}")
