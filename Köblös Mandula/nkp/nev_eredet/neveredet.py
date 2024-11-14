forrás = open('ferfi_nevek_eredete.txt', mode='r', encoding='utf-8')

ferfi_nevek = []
eredet_f = []

for sor in forrás:
    adat = sor.strip().split(',')
    ferfi_nevek.append(adat[0])
    eredet_f.append(adat[1])

forrás.close()

forrás2 = open('noi_nevek_eredete.txt', mode='r', encoding='utf-8')

noi_nevek = []
eredet_n = []

for sor in forrás2:
    adat = sor.strip().split(',')
    noi_nevek.append(adat[0])
    eredet_n.append(adat[1])

forrás2.close()

for i in range(len(noi_nevek)):
    if 'magyar' in eredet_n[i] and noi_nevek[i][0] == 'M' and len(noi_nevek[i]) <= 6:
        print(noi_nevek[i])