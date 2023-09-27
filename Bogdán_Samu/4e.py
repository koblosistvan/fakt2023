szoveg = str(input('Ide írja a szöveget: '))
mgnhangzok = 'aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ'
mgnhangzo = 0
gy = 0
for i in range(len(szoveg)):
    if szoveg[i] in mgnhangzok:
        mgnhangzo += 1
for i in range(len(szoveg) - 1):
    if szoveg[i] in ('g', 'G') and szoveg[i + 1] in ('y', 'Y'):
        gy += 1
print(f'Magánhangzók száma: {mgnhangzo}')
print(f'"Gy" betűk száma: {gy}')
