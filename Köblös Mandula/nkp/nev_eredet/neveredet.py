forrás = open('ferfi_nevek_eredete.txt', mode='r', encoding='utf-8')

ferfi_nevek = []

for sor in forrás:
    ferfi_nevek.append(sor.strip().split(','))

forrás.close()

forrás2 = open('noi_nevek_eredete.txt', mode='r', encoding='utf-8')

noi_nevek = []

for sor in forrás2:
    noi_nevek.append(sor.strip().split(','))

forrás2.close()


def NevKivalaszt(nevlista, kezdobetu, maxhossz, nem, eredet):
    for i in range(len(nevlista)):
        if eredet in eredet_n[i] and noi_nevek[i][0] == 'M' and len(noi_nevek[i]) <= 6:
            print(noi_nevek[i])