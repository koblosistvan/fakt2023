forras1 = open('ferfi_nevek_eredete.txt', mode='r', encoding='utf-8')

forras2 = open('noi_nevek_eredete.txt', mode='r', encoding='utf-8')

noi_nevek = []
ferfi_nevek = []

noi_eredetek = []
ferfi_eredetek = []

for sor in forras1:
    adat = sor.strip().split(',')
    ferfi_eredetek.append(adat[1])
    ferfi_nevek.append(adat[0])

for sor in forras2:
    adat = sor.strip().split(',')
    noi_nevek.append(adat[0])
    noi_eredetek.append(adat[1])

forras1.close()
forras2.close()

jo_noi = []

for i in range(len(noi_nevek)):
    if 'magyar' in noi_eredetek[i] and noi_nevek[i][0] == 'M'and len(noi_nevek) <= 6 :
        jo_noi.append(noi_nevek[i])

print(jo_noi)

