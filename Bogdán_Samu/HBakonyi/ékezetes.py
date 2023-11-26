def szűr(mondat):
    ékezetes = 'áéíóőúűÁÉÍÓŐÚŰ'
    for i in range(len(mondat)):
        for e in range(len(mondat[i])):
            if mondat[i][e] in ékezetes:
                mondat[i] = len(mondat[i]) * '*'
    return ' '.join(mondat)

mondat = list(input('Mondat: ').split(' '))
print(szűr(mondat))
