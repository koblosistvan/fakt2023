forras = open('top100utonev_2011.txt', mode='r', encoding='utf-8')

utonev_2011 = []

for sor in forras:
    utonev_2011.append(sor.strip().split('\t'))

forras.close()

forras2 = open('top100utonev_2021.txt', mode='r', encoding='utf-8')

utonev_2021 = []

for sor in forras2:
    utonev_2021.append(sor.strip().split('\t'))

forras2.close()

mindkettoben = []

for i in range(len(utonev_2021)):
    for j in range(len(utonev_2011)):
        if utonev_2021[i][0] == utonev_2011[j][0]:
            mindkettoben.append(utonev_2021[i][0])
            break
print(mindkettoben)
print(len(mindkettoben))


#2. feladat


print(utonev_2021)
for i in range(len(utonev_2021) - 1):
    max = i
    for j in range(i + 1, len(utonev_2021)):
        if int(utonev_2021[j][1]) > int(utonev_2021[max][1]):
            max = j

    seged = utonev_2021[i]
    utonev_2021[i] = utonev_2021[max]
    utonev_2021[max] = seged

print(utonev_2021)

kiiras = open('ferfi_2021.txt', mode='w', encoding='utf-8')

for i in range(len(utonev_2021)):