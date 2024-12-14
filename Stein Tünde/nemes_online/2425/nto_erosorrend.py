elso = input().split(' ')
n = int(elso[0])
m = int(elso[1])
tagok = []
masodik = input().split(' ')
for i in range(len(masodik)):
    tagok.append(masodik[i])
tagokmasolat = tagok.copy()
t = []
k = []
for i in range(m):
    harmadik = input()
    if '>' in harmadik:
        t.append(harmadik.split('>')[0].strip())
        k.append(harmadik.split('>')[1].strip())
    elif '<' in harmadik:
        k.append(harmadik.split('<')[0].strip())
        t.append(harmadik.split('<')[1].strip())
sorrend = tagok.copy()
for i in range(len(sorrend)):
    for z in range(len(sorrend)):
        for j in range(len(k)):
            if sorrend[i] == t[j] and sorrend[z] == k[j]:
                sorrend[i], sorrend[z] = sorrend[z], sorrend[i]

print(sorrend)


"""for i in range(len(tagokmasolat)-1):
    for j in range(i, len(tagokmasolat)):
        for z in range(len(k)):
            if tagokmasolat[i] == t[z] and tagokmasolat[j] == k[z]:
                tagokmasolat[i], tagokmasolat[z] = tagokmasolat[z], tagokmasolat[i]
print(tagokmasolat)

tobb = t.copy()
kevesebb = k.copy()

sorrend = tagok.copy()
tobbek = [0]*len(tagok)
kevesebbek = [0]*len(tagok)
volt1 = []
volt2 = []
for i in range(len(tagok)):
    for k in range(len(tobb)):
        a = tagok[i]
        b = tobb[k]
        if tagok[i] == tobb[k]:
            if tagok[i] not in volt1:
                tobbek[i] = tobb.count(tobb[k])
                volt1.append(tobb[k])
        if tagok[i] == kevesebb[k] and tagok[i] not in volt2:
            kevesebbek[i] = kevesebb.count(kevesebb[k])
            volt2.append(kevesebb[k])
for i in range(len(tobbek)-1):
    for k in range(len(tobbek)-1):
        if tobbek[k] > tobbek[k+1]:
            tobbek[k], tobbek[k+1] = tobbek[k+1], tobbek[k]
            sorrend[k], sorrend[k + 1] = sorrend[k + 1], sorrend[k]
        elif tobbek[k] == tobbek[k+1]:
            if sorrend[k] > sorrend[k+1]:
                sorrend[k], sorrend[k+1] = sorrend[k+1], sorrend[k]
                tobbek[k], tobbek[k + 1] = tobbek[k + 1], tobbek[k]
print(*sorrend)
"""
"""
6 5
Andrea Bea Csilla Hanna Lilla Viki
Csilla > Lilla
Hanna < Lilla
Bea > Viki
Andrea > Bea
Andrea < Hanna


3 3
Albert Bence Cecil
Albert > Bence
Bence < Cecil
Cecil < Albert
"""
