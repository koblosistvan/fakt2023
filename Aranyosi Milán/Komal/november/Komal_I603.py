szamok = input('Add meg melyik két szám szimpátiáját szeretnéd megtudni: ')

elso_szam = 0
masodik_szam = 0

for i in range(len(szamok)):
    adat = szamok.strip().split(' ')
    elso_szam = int(adat[0])
    masodik_szam = int(adat[1])

def nullaeleje(szam):
    if szam[0] == '0' and szam != '0':
        return False
    else:
        return True

def szetszedes(szam):
    x = []
    for szamjegy in range(len(szam)):
        for a in range(szamjegy + 1, len(szam) + 1):
            s = szam[szamjegy:a]
            if nullaeleje(s):
                x.append(int(s))
    return x

def szimpatia(elso_szam, masodik_szam):
    szimp = 0
    for i in range(len(elso_szam)):
        for j in range(len(masodik_szam)):
            if masodik_szam[j] == 0:
                continue
            if elso_szam[i] % masodik_szam[j] == 0:
                szimp += 1

    for i in range(len(masodik_szam)):
        for j in range(len(elso_szam)):
            if elso_szam[j] == 0:
                continue
            if masodik_szam[i] % elso_szam[j] == 0:
                szimp += 1
    return szimp

print(f'A {elso_szam} és {masodik_szam} szimpátiája: {szimpatia(szetszedes(str(elso_szam)), szetszedes(str(masodik_szam)))}')
