mondat = input('Add meg a mondatot:')

uj_mondat = ''

for i in range(len(mondat)):
    uj_mondat += chr(ord(mondat[i])+3)

print(uj_mondat)

