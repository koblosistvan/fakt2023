forras = open('kerekparverseny.txt', mode='r', encoding='utf-8')

elso_sor = forras.readline().strip().split()

varosok_szama = int(elso_sor[0])

verseny_hossz = int(elso_sor[1])

varosok_tavolsaga = []

for sor in forras:
    varosok_tavolsaga.append(int(sor.strip()))

#print(varosok_szama, varosok_tavolsaga, verseny_hossz)

megfelelo_varsosok = []

for i in range(len(varosok_tavolsaga)-1):
    ket_varos_tav = varosok_tavolsaga[i] + varosok_tavolsaga[i+1]
    if ket_varos_tav < verseny_hossz:
        ket_varos_tav + varosok_tavolsaga[i+2]

    elif ket_varos_tav == verseny_hossz:
        megfelelo_varsosok.append(i, i+1)

