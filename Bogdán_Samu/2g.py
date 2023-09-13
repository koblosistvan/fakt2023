x = int(input("Első szám: "))
y = int(input("Második szám: "))
if x >= y and x % y == 0:
    print("Az első szám osztható a második számmal.")
if y >= x and y % x == 0:
    print("A második szám osztható az első számmal.")
if x % y != 0 and y % x != 0:
    print("A két szám nem osztahtó egymással.")
