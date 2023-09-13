a = 2
b = 8

while True:
    b_összeg = int(input("Mennyi a két szám összege? "))

    if b_összeg == a + b:
        print("Jap")
        break
    elif abs(b_összeg - (a + b) < 10):
        print("Közel.")
    else:
        print("Nop")
        



