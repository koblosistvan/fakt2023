# 1. feladat
# Olvassa be a forgalom.txt állományban talált adatokat, s azok felhasználásával oldja
# meg a következő feladatokat! Ha az állományt nem tudja beolvasni, akkor az első 10 sorának
# adatait jegyezze be a programba és dolgozzon azzal!
időpont = []
áthaladás = []
irány = []
óra = []

def idő2mp(ó, p, mp):
    return ó*3600 + p*60 + mp

forrás = open('forgalom.txt', mode='r', encoding='utf-8')
forrás.readline()
for sor in forrás:
    adat = sor.strip().split(' ')
    időpont.append(idő2mp(int(adat[0]), int(adat[1]), int(adat[2])))
    áthaladás.append(int(adat[3]))
    irány.append(adat[4])
    óra.append(int(adat[0]))
forrás.close()


# 2. feladat
# Írja ki a képernyőre, hogy az n-edikként belépő jármű melyik város felé haladt! Ehhez
# kérje be a felhasználótól az n értékét!
print('2. feladat')
n = int(input('Adja meg a jármű sorszámát: '))
n_irány = 'Alsó város' if irány[n-1] == 'F' else 'Felső város'
print(f'A {n}. jármű {n_irány} irányába haladt.')

# 3. feladat
# Írja a képernyőre, hogy a Felső város irányába tartó utolsó két jármű hány másodperc
# különbséggel érte el az útszakasz kezdetét!
felső_felé = []
i = len(időpont)
while len(felső_felé) < 2:
    i -= 1
    if irány[i] == 'A':
        felső_felé.append(időpont[i])
print('\n3. feladat')
print(f'A két utolsó Felső város felé tartó jármű {felső_felé[0] - felső_felé[1]} másodperc különbséggel érte el az útszakaszt.')


# 4. feladat
# Határozza meg óránként és irányonként, hogy hány jármű érte el a szakaszt! Soronként
# egy-egy óra adatait írja a képernyőre! Az első érték az órát, a második érték az Alsó,
# a harmadik a Felső város felől érkező járművek számát jelentse! A kiírásban csak azokat
# az órákat jelenítse meg, amelyekben volt forgalom valamely irányban!

# 5. feladat
# A belépéskor mért értékek alapján határozza meg a 10 leggyorsabb járművet! Írassa ki a
# képernyőre ezek belépési idejét, a várost (Alsó, illetve Felső), amely felől érkezett,
# és m/s egységben kifejezett sebességét egy tizedes pontossággal, sebességük szerinti
# csökkenő sorrendben! Ha több azonos sebességű járművet talál, bármelyiket megjelenítheti.
# Soronként egy jármű adatait jelenítse meg, és az egyes adatokat szóközzel tagolja!
# (A feladat megoldásakor figyeljen arra, hogy a következő feladatban az adatok eredeti
# sorrendjét még fel kell használni!)

# 6. feladat
# Írassa ki az also.txt állományba azokat az időpontokat, amikor az Alsó város felé tartók
# elhagyták a kérdéses útszakaszt! Ha egy jármű utolér egy másikat, akkor a kilépésük
# időpontja a lassabb kilépési ideje legyen! A fájl minden sorába egy-egy időpont kerüljön
# óra perc másodperc formában! A számokat pontosan egy szóköz válassza el egymástól!
