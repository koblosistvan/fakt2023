mondat = 'Jaj de jó hír'
szavak = mondat.split(' ')
for i in range(len(szavak)):
    betűk = list(x for x in szavak[i])
    for j in range(len(betűk)):
        if