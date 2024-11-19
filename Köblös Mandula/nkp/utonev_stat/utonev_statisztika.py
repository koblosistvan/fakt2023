forrás = open('top100utonev_2011.txt', mode='r', encoding='utf-8')

utonev_2011 = []

for sor in forrás:
    utonev_2011.append(sor.strip().split('\t'))

forrás.close()

forrás2 = open('top100utonev_2021.txt', mode='r', encoding='utf-8')

utonev_2021 = []

for sor in forrás2:
    utonev_2021.append(sor.strip().split('\t'))

forrás2.close()

#2. feladat
osszesen = 0

for i in range(len(utonev_2011)):
    for j in range(len(utonev_2021)):
        if utonev_2021[j][0] == utonev_2011[i][0]:
            print(utonev_2011[i][0])
            osszesen += 1

print(f'Összesen {osszesen} név szerepel kétszer.')

# 3. feladat
ferfi_2021 = []
noi_2021 = []

for i in range(len(utonev_2021) - 1):
    min = i
    for j in range(i + 1, len(utonev_2021)):
        if utonev_2021[j] < utonev_2021[min]:
            min = j

    seged = utonev_2021[i]
    utonev_2021[i] = utonev_2021[min]
    utonev_2021[min] = seged

print(utonev_2021)

kiiras = open('ferfi_2021.txt', mode='w', encoding='utf-8')

for i in range(len(utonev_2021)):
    if utonev_2021[i][2] == 'F':
        ferfi_2021.append(utonev_2021[i])
    elif utonev_2021[i][2] == 'N':
        noi_2021.append(utonev_2021[i])
