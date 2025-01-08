# Nemes Tihamér Online 2. forduló - 2. feladat - Nomád játék
# Kadarkuti Márton

# bemenet
osszeg:int = int(input().strip())
a:int = int(input().strip())
b:int = int(input().strip())
megoldasok:list[tuple[int]] = []

# a feladat megoldasai azok az (x,y) szamparok, melyre ax+by=osszeg teljesul
# x es y minimum 0, maximum pedig rendre osszeg//a es osszeg//b

for x in range(1+ osszeg//a):
    for y in range(1+ osszeg//b):
        if a*x + b*y == osszeg:
            megoldasok.append( (x,y) )

# kimenet
print(len(megoldasok))
for i in megoldasok:
    print(i[0],i[1])