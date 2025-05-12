parancs = input('Kérem a robot parancsait: ')
eszak = 0
delirany = 0
kelet = 0
nyugat = 0
egyszerusitett =[]
for i in parancs:
    egyszerusitett.append(i)
    if i == "E":
        eszak += 1
    if i == "D":
        delirany += 1
    if i == "K":
        kelet += 1
    if i == "N":
        nyugat += 1
if (eszak and delirany) > 0:
    if eszak > delirany:
        for i in range(eszak if eszak < delirany else delirany):
            egyszerusitett.remove('E')
            egyszerusitett.remove('D')
if (kelet and nyugat) > 0:
    if kelet > nyugat:
        for i in range(kelet if kelet < nyugat else nyugat):
            egyszerusitett.remove('K')
            egyszerusitett.remove('N')


print(f'E betűk száma: {eszak}\nD betűk száma: {delirany}\nK betűk száma: {kelet}\nN betűk száma: {nyugat}\n'
      f'Egy legrövidebb út parancsszava: {"".join(sorted(egyszerusitett)    )}')