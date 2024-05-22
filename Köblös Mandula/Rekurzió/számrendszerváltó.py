def valtas(szam, alap):
    if szam < alap:
        print(szam, end='')
    else:
        valtas(szam // alap, alap)
        print(szam % alap, end='')

print(valtas(517, 2))