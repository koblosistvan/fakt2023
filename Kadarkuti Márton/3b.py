a = int(input("Kezdőpont: "))
b = int(input("Végpont: "))
c = int(input("Hányasával?: "))

a,b,c = abs(a), abs(b), abs(c)

print("")

for i in range(a, b+1, c):
    print(i)

print(":Vége:")