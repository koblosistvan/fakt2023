tagok_száma, párok_száma = [int(s) for s in input().split()]
tagok = input().split()
kisebbek, nagyobbak = [], []
for _ in range(párok_száma):
    mérés = input().split()
    if mérés[1] == '<':
        kisebbek.append(mérés[0])
        nagyobbak.append(mérés[2])
    else:
        kisebbek.append(mérés[2])
        nagyobbak.append(mérés[0])

sorrend = []
for t in range(tagok_száma):
    vesztesek = list(set(tagok) - set(nagyobbak))
    if len(vesztesek) == 1:
        tag = vesztesek[0]
        sorrend.append(tag)
        tagok.remove(tag)
        k, n = [], []
        for i in range(len(kisebbek)):
            if kisebbek[i] != tag:
                k.append(kisebbek[i])
                n.append(nagyobbak[i])
        kisebbek, nagyobbak = k, n

if len(tagok):
    print('Ketseges')
else:
    print(' '.join(sorrend))

'''
teszt 1
3 3
Albert Bence Cecil
Albert > Bence
Bence < Cecil
Cecil < Albert

teszt 2
6 5
Andrea Bea Csilla Hanna Lilla Viki
Csilla > Lilla
Hanna < Lilla
Bea > Viki
Andrea > Bea
Andrea < Hanna

teszt 3
8 12
Be Er Rn Nh Ha Ar Rd Db
Be > Er
Er > Rn
Rn > Nh
Rn > Ha
Rn > Ar
Rn > Rd
Rn > Db
Nh > Ar
Ha > Ar
Ar > Rd
Ar > Db
Db < Rd

'''