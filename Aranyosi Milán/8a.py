forras = open('8a-kártyák.txt', mode='r', encoding='utf-8')

kartyak = []

for sor in forras:
    adat = sor.strip().split()
    kartyak.append(int(adat[0]))
print(kartyak)

for i in range(len(kartyak), 0, -1):
    for j in range(i-1):
        if kartyak[j] > kartyak[j+1]:
            kartyak[j], kartyak[j+1] = kartyak[j+1], kartyak[j]
            print(kartyak)
print(kartyak)
