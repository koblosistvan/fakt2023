top100utonev2011 = open("PigaiPéter\\top100utonev_2011.txt", mode='r', encoding='utf-8')
top100utonev2021 = open("PigaiPéter\\top100utonev_2021.txt", mode='r', encoding='utf-8')

név2011 = []
név2021 = []
névmennyiség2011 = []
névmennyiség2021 = []
nem2011 = []
nem2021 = []

for sor in top100utonev2011:
    elem = sor.strip().split('\t')
    név2011.append(elem[0])
    névmennyiség2011.append(int(elem[1]))
    nem2011.append(elem[2])
top100utonev2011.close()
for sor in top100utonev2021:
    elem = sor.strip().split('\t')
    név2021.append(elem[0])
    névmennyiség2021.append(int(elem[1]))
    nem2021.append(elem[2])
top100utonev2021.close

név2021set = set(név2021)
név2011set = set(név2011)
metszet = név2021set.intersection(név2011set)
metszet = list(metszet)
print(f"Mindkét évben szerepeltek:{', '.join(metszet)} \nNevek száma:{len(metszet)}")

noi = open('PigaiPéter\\noi_2021.txt', 'w', encoding='utf-8')
ferfi = open('PigaiPéter\\ferfi_2021.txt', 'w', encoding='utf-8')

noinevek = []
noidarab = []
noidarab1 = []
n_ind = []

ferfinevek = []
ferfidarab = []
ferfidarab1 = []
f_ind = []

for i in range(len(név2021)):
    if nem2021[i] == 'N':
        noinevek.append(név2021[i])
        noidarab.append(névmennyiség2021[i])
        noidarab1.append(névmennyiség2021[i])
    elif nem2021[i] == 'F':
        ferfinevek.append(név2021[i])
        ferfidarab.append(névmennyiség2021[i])
        ferfidarab1.append(névmennyiség2021[i])

noidarab1.sort()
noidarab1.reverse()
ferfidarab1.sort()
ferfidarab1.reverse()

for i in range(len(noidarab)):
    n_ind.append(noidarab.index(noidarab1[i]))
for i in range(len(ferfidarab)):
    f_ind.append(ferfidarab.index(ferfidarab1[i]))

for i in range(len(ferfidarab)):
    ferfi.write(ferfinevek[f_ind[i]] + '\n')
for i in range(len(noidarab)):
    noi.write(noinevek[n_ind[i]] + '\n')

noi.close()
ferfi.close()

