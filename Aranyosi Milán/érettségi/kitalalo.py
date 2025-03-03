import random

szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas", "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]

rejtett_szo = random.choice(szavak)

tipp = input('Kérem a tippet: ')

eredmeny = ''
kor_szamlalo = 1
stop_szaml = 0

while tipp != rejtett_szo:
    if tipp == 'stop':
        stop_szaml += 1
        break
    for i in range(6):
        if tipp[i] == rejtett_szo[i]:
            eredmeny += rejtett_szo[i]
        else:
            eredmeny += '.'


    print(f'Az eredmény: {eredmeny}\n')
    eredmeny = ' '
    kor_szamlalo += 1
    tipp = input('Kérem a tippet: ')

if stop_szaml == 1:
    pass
else:
    print(f'{kor_szamlalo} tippeléssel sikerült kitalálni.')


