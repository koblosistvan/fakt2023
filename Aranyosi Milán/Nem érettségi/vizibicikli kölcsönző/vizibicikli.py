class Kolcsonzes:
    def __init__(self, nev, azonosito, e_ora, e_perc, v_ora, v_perc):
        self.nev = nev
        self.azonosito = azonosito
        self.e_ora = e_ora
        self.e_perc = e_perc
        self.v_ora = v_ora
        self.v_perc = v_perc


def ido(ora,perc):
    return ora*60 + perc

kolcsonzesek = []
forras = open('kölcsönzések', mode='r', encoding='utf-8')
forras.readline()
for sor in forras:
    adat = sor.strip().split(';')
    kolcsonzesek.append(Kolcsonzes(nev=adat[0], azonosito=adat[1], e_ora=int(adat[2]), e_perc=int(adat[3]), v_ora=int(adat[4]), v_perc=int(adat[5])))
forras.close()

#5. feladat
print(f'Az állomány {len(kolcsonzesek)} kölcsönzés adatait tartalmazza.')

#6. feladat
bekert_nev = input('Add meg a nevet: ')
szamlalo = 0
for i in range(len(kolcsonzesek)):
    if bekert_nev in kolcsonzesek[i].nev:
        print(f'{bekert_nev} a vizibiciklit {kolcsonzesek[i].e_ora}:{kolcsonzesek[i].e_perc}-kor vitte el és {kolcsonzesek[i].v_ora}:{kolcsonzesek[i].v_perc}-kor hozta vissza.')
        szamlalo += 1
if szamlalo == 0:
    print('Nem volt ilyen nevű kölcsönző.')

#7. feladat
bekert_ido = input('Add meg melyik időpontra vagy kíváncsi:')
resz = bekert_ido.strip().split(':')
ora = resz[0]
perc = resz[1]
bekert_ido_percben = int(ora)*60 + int(perc)

