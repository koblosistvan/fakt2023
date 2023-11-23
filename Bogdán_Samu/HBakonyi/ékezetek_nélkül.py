def szűr(mondat):
    ékezetes = 'áéíóőúűÁÉÍÓŐÚŰ'
    for i in range(len(mondat)):
        for e in range(len(list(mondat[i]))):
            if list(mondat[i])[e] in ékezetes:
                for f in range(len(mondat[i])):
                    list(mondat[i])[f] = '*'
    return ' '.join(mondat)

mondat = list(input('Mondat: ').split(' '))
print(szűr(mondat))
