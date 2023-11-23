def szűr(mondat):
    szavak = mondat.split(' ')
    cenzurazott =[]
    for i in range(len(szavak)):
        betűk = list(x for x in szavak[i])
        for j in betűk:
            if j == 'Á' or j == 'É' or j == 'Ő' or j == 'Ű' or j == 'Í' or j == 'Ó' or j == 'ó' or j == 'í' or j == 'á'\
                    or j == 'é' or j == 'ő' or j == 'ű':
                betűk = len(betűk)*'!'
                break
        betűk = ''.join(betűk)
        cenzurazott.append(betűk)
    return ' '.join(cenzurazott)


