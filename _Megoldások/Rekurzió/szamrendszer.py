def valtas(szam, alap):
    if szam < alap:
        print(szam, end='')
    else:
        valtas(szam // alap, alap)
        print(szam % alap, end='')


valtas(517, 5)