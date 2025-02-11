# 1
forras = open('melyseg.txt', 'r', encoding='utf-8')
melysegek = []
for i in forras:
    sor = i.strip()
    melysegek.append(int(sor))
forras.close()
print(f'1. feladat\nA fájl adatainak száma: len(melysegek)')


"""1. feladat 
A fájl adatainak száma: 694 
2. feladat 
Adjon meg egy távolságértéket! 9 
Ezen a helyen a felszín 2 méter mélyen van. 
3. feladat 
Az érintetlen terület aránya 10.09%. 
5. feladat 
A gödrök száma: 22 
6. feladat 
a) 
A gödör kezdete: 7 méter, a gödör vége: 22 méter. 
b) 
Nem mélyül folyamatosan. 
c) 
A legnagyobb mélysége 4 méter. 
d) 
A térfogata 440 m^3. 
e) 
A vízmennyiség 280 m^3. """