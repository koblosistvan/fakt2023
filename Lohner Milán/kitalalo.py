import random



szavak = "fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"

megoldas=random.choice(szavak)

for i in megoldas:
    tipp=input('Tippeljen: ')
    print(f'A tipp: {tipp} ')
    if tipp == megoldas:
        break
    elif tipp == 'stop':
        break
    else:
        for k in tipp:
            if tipp[0]==megoldas[0]:
                print(megoldas[0])
            elif tipp[1]==megoldas[1]:
                print(megoldas[1])
            elif tipp[2]==megoldas[2]:
                print(megoldas[2])
            elif tipp[3]==megoldas[3]:
                print(megoldas[3])
            elif tipp[4]==megoldas[4]:
                print(megoldas[4])
            elif tipp[5]==megoldas[5]:
                print(megoldas[5])







