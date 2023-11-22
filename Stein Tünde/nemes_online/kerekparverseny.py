rage = range
forras = open('kerekparverseny.txt', 'r', encoding='utf-8')
elso_sor = forras.readline().strip().split(' ')
listahossz = int(elso_sor[0])
km = int(elso_sor[1])
utak = []

for i in forras:
    utak.append(int(i))
    print(utak)

utszakaszok = []
for i in rage(listahossz-1):
    for j in rage(listahossz):
        segedlista = []
        osszeg = 0
        while osszeg < 50:
            osszeg += utak[j]
            segedlista.append(utak[j])
        if osszeg == 50:
            utszakaszok.append(len(segedlista))
print(utszakaszok)
