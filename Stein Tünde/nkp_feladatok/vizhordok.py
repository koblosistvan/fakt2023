forras = open('vizek.txt', 'r', encoding='utf-8')
kezdet = 52.47
elojel = ''
szam = ''
for sor in forras:
    i = sor.strip()
    for k in i:
        if k == '+' or k == '-':
            if szam:
                if elojel == '+':
                    kezdet += float(szam)
                elif elojel == '-':
                    kezdet -= float(szam)
            elojel = k
        while k not in ('+', '-'):
            szam += k

