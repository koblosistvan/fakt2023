x = open('Bogdán_Samu\\órai\\utonevek\\utonevek.txt', 'r', encoding='utf-8')
y = open('Bogdán_Samu\\órai\\utonevek\\nevek.txt', 'w', encoding='utf-8')
nev = input('> ')
for i in x:
    if len(i.strip()) + len(nev) <= 30:
        y.write(f'{nev} {i.strip()}'+'\n')
x.close()
y.close()