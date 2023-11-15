forras = open('7a-lakas-arak.txt', 'r', encoding='utf-8')

forras.readline()
alapt = []
ar = []

for i in forras:
    sor = i.strip().split(' ')
    alapt.append(int(sor[0]))
    ar.append(int(sor[1]))

forras.close()
print(f'{ar.index(min(ar))}.ház a legolcsobb, {min(ar)} millio forint')
print(f'{ar.index(max(ar))}.ház a legdragabb, {max(ar)} millio forint')



print(alapt)
print(ar)

vanotszaz = False
for i in range(len(ar)):
    if ar[i] > 500:
        vanotszaz == True
if vanotszaz:
    print('van 500m-nál drágább')
else:
    print('nincs 500m-nál drágább')

arterulet = []
for i in range(len(alapt)-1):
    arterulet.append(ar[i]/alapt[i])
print(max(arterulet), 'a legmagasabb ár terület arány')

