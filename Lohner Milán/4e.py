szoveg=input('Add meg a szöveget: ')

maganhangzok='aáeéiíoóöőuúóüű'

szamlalo=0

for i in range(len(szoveg)):
    if szoveg[i].lower() in (maganhangzok):
        print(szoveg[i], end='')


for i in range(len(szoveg)):
    if szoveg[i].lower() in (maganhangzok):
        szamlalo += 1

print(f'Ennyi db: {szamlalo}')

gyszama=0
g='g'
y='y'

for i in range(len(szoveg)):
    if szoveg[i] in (g) and szoveg[i+1] in (y):
        gyszama += 1
        print(f'Gy betűk száma: {gyszama}')



