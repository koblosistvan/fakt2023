forrás = open('8a-kártyák.txt', mode='r', encoding='utf-8')

kártyák = []

for sor in forrás:
    kártyák.append(int(sor.strip()))
forrás.close()

print(kártyák)

for i in range(len(kártyák), 0, -1):
    for j in range(i-1):
        if kártyák[j] > kártyák[j+1]:
            kártyák[j], kártyák[j+1] = kártyák[j+1], kártyák[j]
            print(kártyák)

print(kártyák)