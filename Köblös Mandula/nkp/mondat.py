mondat = input('Írj egy mondatot! ')

uj = ''

for i in range(len(mondat)):
    uj += chr(ord(mondat[i])+3)

print(uj)