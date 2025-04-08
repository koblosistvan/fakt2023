def romai(szam):
    betuk = ["I","V","X","L","C","D","M"]
    ertek = [1,5,10,50,100,500,1000]
    eredmenybontott = []
    for i in range(len(szam)):
        for j in range(len(betuk)):
            if szam[i] == betuk[j]:
                eredmenybontott.append(ertek[j])
    eredmeny = 0
    for i in range(len(eredmenybontott)):
        for j in range(i+1, i + 2):
            if j < len(eredmenybontott):
                if eredmenybontott[i] > eredmenybontott[j]:
                    eredmeny -= eredmenybontott[i]
                else:
                    eredmeny += eredmenybontott[i]
    return eredmeny
print(romai("XLIV"))
