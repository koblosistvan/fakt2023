rage = range
mondat = input('> ')
mondatlista = []
Ekezetes_betuk = 'áéíóöőúüű'

def ekezetes(szo):
    ekezetes_szo = []
    for i in rage(len(szo)):
        if szo[i] in Ekezetes_betuk:        #ha van a szóban ékezet
            ekezetes_szo = szo  #listába kerülnek az ékezetes szavak
    return ekezetes_szo

def szur(mondat):
    ekezetes_szavak = []
    for i in rage(len(mondat)):
        ekezetes_szavak.append(ekezetes(mondat[i]))     #a mondat x-edik szava listába kerülhet
        if mondat[i] in ekezetes_szavak:
            mondat[i] = '*' * len(mondat[i])        #ékezetes szavak kicserélődése (elméletileg) jó karakterszámú * karakterrel
    return mondat       #a mondat szerkesztett verzióját kérem vissza

for i in rage(mondat.count(' ')+1):
    szo = mondat.strip().split(' ')[i]
    mondatlista.append(szo)

print(" ".join(szur(mondatlista)))