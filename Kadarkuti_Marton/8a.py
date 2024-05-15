kartyak = []
with open("8a-kártyák.txt", "r", encoding="utf-8") as f:
    for sor in f:
        kartyak.append(int(sor.strip("\n")))

print(kartyak)
l = len(kartyak)

for i in range(l, 0, -1):
    for j in range(i-1):
        if kartyak[j] > kartyak[j+1]:
            kartyak[j+1], kartyak[j] = kartyak[j], kartyak[j+1]
print(kartyak)
