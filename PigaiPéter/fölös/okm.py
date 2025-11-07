class Okm:
    def __init__(self, azonosito: str, sz_p_e: str, sz_p_v: str, sz_p_t:int, m_p_e: str, m_p_v: str, m_p_t: int, m_e_p: str, m_v_p: str):
        self.azonosito = azonosito
        self.sz_p_e = sz_p_e
        self.sz_p_v = sz_p_v
        self.sz_p_t = sz_p_t
        self.m_p_e = m_p_e
        self.m_p_v = m_p_v
        self.m_p_t = m_p_t
        self.m_e_p = m_e_p
        self.m_v_p = m_v_p

forras = open('PigaiPéter\\okm-2023-7.csv', 'r', encoding='utf-8')
forras.readline()
forras.readline()
forras.readline()
adatok = []
for sor in forras:
    adat = sor.strip().split(';')
    adatok.append(Okm(azonosito=str(adat[2]),sz_p_t=int(adat[3]), sz_p_e=str(adat[5]), sz_p_v=str(adat[7]), m_p_t=int(adat[9]), m_p_e=str(adat[11]), m_e_p=str(adat[12]), m_p_v=str(adat[13]), m_v_p=str(adat[14])))

#
print(f'{len(set(adatok))} diák van a fájlban')

#
pontok = []
for i in range(len(adatok)):
    if adatok[i].sz_p_v == 'Nincs':
        pontok.append(int(adatok[i].sz_p_e))
    else:
        pontok.append(int(adatok[i].sz_p_v))
print(f'{adatok[pontok.index(max(pontok))].azonosito} azonosítójú diák pontszáma a legmagasabb')

#
változott = 0
for i in range(len(adatok)):
    if adatok[i].sz_p_v != 'Nincs' and adatok[i].sz_p_v != adatok[i].sz_p_e:
        változott += 1
print(f'{változott} diáknak változott a pontszáma')

#
for i in range(len(adatok)):
    if adatok[i].sz_p_v == 'Nincs':
        if adatok[i].m_p_v == 'Nincs':
            if (int(adatok[i].sz_p_e) > adatok[i].sz_p_t and int(adatok[i].m_p_e) < adatok[i].m_p_t) or (int(adatok[i].sz_p_e) < adatok[i].sz_p_t and int(adatok[i].m_p_e) > adatok[i].m_p_t):
                print(adatok[i].azonosito)
        else:
            if (int(adatok[i].sz_p_e) > adatok[i].sz_p_t and int(adatok[i].m_p_v) < adatok[i].m_p_t) or (int(adatok[i].sz_p_e) < adatok[i].sz_p_t and int(adatok[i].m_p_v) > adatok[i].m_p_t):
                print(adatok[i].azonosito)
    else:
            if adatok[i].m_p_v == 'Nincs':
                if (int(adatok[i].sz_p_v) > adatok[i].sz_p_t and int(adatok[i].m_p_e) < adatok[i].m_p_t) or (int(adatok[i].sz_p_v) < adatok[i].sz_p_t and int(adatok[i].m_p_e) > adatok[i].m_p_t):
                    print(adatok[i].azonosito)
            else:
                if (int(adatok[i].sz_p_v) > adatok[i].sz_p_t and int(adatok[i].m_p_v) < adatok[i].m_p_t) or (int(adatok[i].sz_p_v) < adatok[i].sz_p_t and int(adatok[i].m_p_v) > adatok[i].m_p_t):
                    print(adatok[i].azonosito)

#
volt = False
for i in range(len(adatok)):
    if adatok[i].m_p_v == 'Nincs':
        if adatok[i].m_p_t - int(adatok[i].m_p_e) > 150:
            volt = True
            break
    else:
        if adatok[i].m_p_t - int(adatok[i].m_p_v) > 150:
            volt = True
            break
if volt:
    print('Volt olyan diák aki 150 pontnál többet rontott')
else:
    print('Nem volt olyan diák aki 150 pontnál többet rontott')

#
szintfajtak = set()
szintek = []
for i in range(len(adatok)):
    if adatok[i].m_v_p == 'Nincs':
        szintfajtak.add(adatok[i].m_e_p)
        szintek.append(adatok[i].m_e_p)
    else:
        szintfajtak.add(adatok[i].m_v_p)
        szintek.append(adatok[i].m_v_p)
szintfajtak = sorted(list(szintfajtak))
legtöbb = 0
for i in range(len(szintfajtak)):
    if szintek.count(szintfajtak[i]) > legtöbb:
        legtöbb = szintek.count(szintfajtak[i])
for i in range(len(szintfajtak)):
    print(f'{szintfajtak[i]} {szintek.count(szintfajtak[i]) : >10} {round(szintek.count(szintfajtak[i]) / legtöbb * 10) * "%"}')

#


#
kiir = open('PigaiPéter\\javítottak.txt', 'w', encoding='utf-8')
javítottak = []
for i in range(len(adatok)):
    if adatok[i].m_p_v == 'Nincs':
        if int(adatok[i].m_p_e) - adatok[i].m_p_t > 100:
            javítottak.append(f'{adatok[i].azonosito} ')
            javítottak.append(f'{adatok[i].m_p_t} {adatok[i].m_p_e}')
            javítottak.append('\n')
kiir.write(''.join(javítottak))

