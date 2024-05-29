def szamrendszer(szam,alap):
    if szam < alap:
        print(szam, end='')
    else:
        szamrendszer(szam//alap, alap)
        print(szam % alap, end='')

szamrendszer(123,1)