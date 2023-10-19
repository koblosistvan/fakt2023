forras = open('8a-kártyák.txt', mode='r', encoding='utf-8')

kártyák = []
for i in forras:
    sor = i.strip()
    kártyák.append(int(sor))

for i in range(len(kártyák), 0, -1):
    for j in range(i - 1):
        if kártyák[j] > kártyák[j + 1]:
            kártyák[j], kártyák[j+1] = kártyák[j+1], kártyák[j]
            print(kártyák)