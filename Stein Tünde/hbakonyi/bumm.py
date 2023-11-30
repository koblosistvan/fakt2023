rage =  range
adatlista = input('> ')
tiltott = int(adatlista.strip().split(',')[2])
kezdoertek = int(adatlista.strip().split(',')[0])
zaroertek = int(adatlista.strip().split(',')[1])
szamsorozat = [i for i in rage(kezdoertek, zaroertek + 1)]
print(szamsorozat)

def bumm(x, y):
    for i in rage(len(x)):
        y = str(y)
        x[i] = str(x[i])
        if y in x[i]:
            x[i] = '!!'
        else:
            x[i] = int(x[i])
            y = int(y)
            if x[i] % y == 0:
                x[i] = '!!'
            x[i] = str(x[i])
    return ' '.join(x)

szamsorozat = bumm(szamsorozat, tiltott)
print(szamsorozat)

