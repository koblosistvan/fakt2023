# 1
forras = open('Stein Tünde/érettségi/info/2019infemelttav/4_eUtazas/utasadat.txt', 'r', encoding='utf-8')
megallo = []
felszallas = []
azon = []
tipus = []
ervenyes = []
for i in forras:
    sor  = i.strip().split(' ')
    megallo.append(int(sor[0]))
    felszallas.append(sor[1])
    azon.append(int(sor[2]))
    tipus.append(sor[3])
    ervenyes.append(sor[4])
forras.close()

# 2
print(f'2. feladat\nA buszra {len(felszallas)} utas akart felszállni.')

# 3
def ervenyesseg(x):
    if x <= 10:
        if x == 0:
            return 0
    else:
        


counter = 0
datumok = []
for i in ervenyes:
    if not int(i):
        counter += 1
    elif int(i) > 10:
        datum = f'{i[:4]}.{i[4:6]}.{i[6:]}.'
        if datum < '2019.10.22.':
            counter += 1
        datumok.append(datum)
print(f'3. feladat\nA buszra {counter} utas nem szállhatott fel.')

# 4
megallok = list(set(megallo))
felszallok_szama = [0] * len(megallok)
for i in megallo:
    for k in range(len(megallok)):
        if i == megallok[k]:
            felszallok_szama[k] += 1
maxfelszallok = felszallok_szama.index(max(felszallok_szama))
print(f'4. feladat\nA legtöbb utas ({felszallok_szama[maxfelszallok]} fő) a {megallok[maxfelszallok]}. megállóban próbált felszállni.')

# 5
ingyenes = 0
kedvezmenyes = 0
for i in range(len(tipus)):
    if ervenyes[i] 

"""2. feladat 
A buszra 699 utas akart felszállni. 
3. feladat 
A buszra 21 utas nem szállhatott fel. 
4. feladat 
A legtöbb utas (39 fő) a 8. megállóban próbált felszállni. 
5. feladat 
Ingyenesen utazók száma: 133 fő
A kedvezményesen utazók száma: 200 fő"""