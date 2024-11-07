# lista a számok írásáról
egyesek = ['', 'egy', 'kettő', 'három', 'négy', 'öt', 'hat', 'hét', 'nyolc', 'kilenc']
tizesek = ['', 'tíz', 'húsz', 'harminc', 'negyven', 'ötven', 'hatvan', 'hetven', 'nyolcvan', 'kilencven']
tizenesek = ['', 'tizen', 'huszon', 'harminc', 'negyven', 'ötven', 'hatvan', 'hetven', 'nyolcvan', 'kilencven']

def átalakít(mondat):
    # 1. szétdarabolom szavakra
    szavak = mondat.split(' ')

    # 2. ciklis: minden szóra
    for i in range(len(szavak)):
        # 3. ha szám és 100-nál kisebb, akkor
        if szavak[i].isdigit() and int(szavak[i]) < 100:
            # 4. egyeseket átalakítjuk szöveggé
            szám = egyesek[int(szavak[i][-1])]
            # 5. ha kétjegyű, akkor elé írom a tizeseket betűvel
            if int(szavak[i]) > 9 and szavak[i][-1] == 0:
                szám = tizesek[int(szavak[i][0])]
            elif int(szavak[i]) > 9:
                szám = tizenesek[int(szavak[i][0])] + szám
            szavak[i] = szám
    # 6. visszaalakítom mondattá
    return " ".join(szavak)

print(átalakít("A kertben 40 kutya és 4 macska játszott 100 egérrel."))