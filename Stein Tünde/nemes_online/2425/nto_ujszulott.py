nev1 = input()
nev2 = input()
szovegreszlet = []
indexl = []
nevlista = ['']*(len(nev1)+len(nev2))
for i in range(len(nev2)):
    for k in range(i, len(nev2)):
        sz = nev2[i:k+1]
        if sz in nev1:
            szovegreszlet.append(sz)
            indexl.append(i)
szovegr = szovegreszlet[0]
for i in szovegreszlet:
    if len(i) > len(szovegr):
        szovegr = i
for i in range(indexl[szovegreszlet.index(szovegr)]):
    nevlista[i] = nev2[i]
for i in range(indexl[szovegreszlet.index(szovegr)], indexl[szovegreszlet.index(szovegr)] + len(szovegr)):
    nevlista[i] = szovegr[i]
for i in range(indexl[szovegreszlet.index(szovegr)]+len(szovegr), len(nev2)):
    nevlista[i] = nev2[i]


print(''.join(nevlista))
