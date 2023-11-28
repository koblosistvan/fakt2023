def átalakít(mondat):
    egyesek = ['nulla', 'egy', 'kettő', 'három', 'négy', 'öt', 'hat', 'hét', 'nyolc', 'kilenc']
    tizesek = ['', 'tíz', 'húsz', 'harminc', 'negyven', 'ötven', 'hatvan', 'hetven', 'nyolcvan', 'kilencven']
    tizenesek = ['', 'tizen', 'huszon', 'harminc', 'negyven', 'ötven', 'hatvan', 'hetven', 'nyolcvan', 'kilencven']
    szavak = mondat.split(' ')
    for i in range(len(szavak)):
        if szavak[i].isdigit() and int(szavak[i]) < 100:
            szám = egyesek[int(szavak[i][1])]
            if int(szavak[i]) > 9 and int(szavak[i][-1]) == 0:
                szám = tizesek[int(szavak[i][0])]
            elif int(szavak[i]) > 9 and int(szavak[i][-1]) > 0:
                szám = tizenesek[int(szavak[i][0])] + szám
            szavak[i] = szám
    return " ".join(szavak)

print(átalakít(input('Mondat: ')))
