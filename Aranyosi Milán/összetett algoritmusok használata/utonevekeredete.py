forras1 = open('ferfi_nevek_eredete.txt', mode='r', encoding='utf-8')

forras2 = open('noi_nevek_eredete.txt', mode='r', encoding='utf-8')


noi_nevek = []
ferfi_nevek = []

noi_eredetek = []
ferfi_eredetek = []

jo_noi = []

for sor in forras1:
    adat = sor.strip().split(',')
    ferfi_eredetek.append(adat[1])
    ferfi_nevek.append(adat[0])

for sor in forras2:
    adat = sor.strip().split(',')
    noi_nevek.append(adat[0])
    noi_eredetek.append(adat[1])

#nevlista = input('Melyik listából szeretnél nevet?')
maxhossz = int(input('Milyen hosszú nevet szeretnél?'))
kezdobetu = input('Milyen betűvel kezdődjön a név?')
#nem = input('Milyen nemu?')
eredet = input('Milyen eredetű?')

def nevkivalasztas( maxhossz, kezdobetu, eredet):
    for i in range(len(noi_nevek)):
        if eredet in noi_eredetek[i] and noi_nevek[i][0] == kezdobetu and len(noi_nevek) <= maxhossz:
            return noi_nevek[i]

print(nevkivalasztas(maxhossz, kezdobetu, eredet))

forras1.close()
forras2.close()
