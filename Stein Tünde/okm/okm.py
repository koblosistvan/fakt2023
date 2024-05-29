forras = open('okm.txt', 'r', encoding='utf-8')

meres_id = []
sz_pont22_23 = []
sz_szint22_23 = []
sz_pont23_24 = []
sz_szint23_24 = []
sz_pont_vegleges = []
sz_szint_vegleges = []
m_pont22_23 = []
m_szint22_23 = []
m_pont23_24 = []
m_szint23_24 = []
m_pont_vegleges = []
m_szint_vegleges = []

for i in list(forras)[3:]:
    if i.strip().split(';')[2] not in meres_id:
        meres_id.append(i.strip().split(';')[2])
        k = i.strip().split(';')[3]
        sz_pont22_23.append(int(k))
        k = i.strip().split(';')[4]
        sz_szint22_23.append(int(k))
        k = i.strip().split(';')[5]
        sz_pont23_24.append(int(k))
        k = i.strip().split(';')[6]
        sz_szint23_24.append(int(k))
        if i.strip().split(';')[7] != 'Nincs':
            k = i.strip().split(';')[7]
            k = int(k)
        else:
            k = None
        sz_pont_vegleges.append(k)

        if i.strip().split(';')[8] != 'Nincs':
            k = i.strip().split(';')[8]
            k = int(k)
        else:
            k = None
        sz_szint_vegleges.append(k)

        m_pont22_23.append(i.strip().split(';')[9])
        m_szint22_23.append(i.strip().split(';')[10])
        m_pont23_24.append(i.strip().split(';')[11])
        m_szint23_24.append(i.strip().split(';')[12])
        if i.strip().split(';')[13] != 'Nincs':
            k = i.strip().split(';')[13]
            k = int(k)
        else:
            k = None
        m_pont_vegleges.append(k)

        if i.strip().split(';')[14] != 'Nincs':
            k = i.strip().split(';')[14]
            k = int(k)
        else:
            k = None
        m_szint_vegleges.append(k)

forras.close()


def max2(x):
    kimenet = 0
    for j in range(len(x)):
        if x[j] and x[j] > kimenet:
            kimenet = x[j]
    return x.index(kimenet)


# task 2
print(f'{len(set(meres_id))} diák eredményei vannak a fájlban.')

# task 3
print(f'A(z) {meres_id[max2(sz_pont_vegleges)]} '
      f'azonosítójú diáknak a legmagasabb a szövegértés pontszáma.')

# task 4
counter = 0
for i in range(len(meres_id)):
    if sz_szint23_24[i] != sz_szint_vegleges[i]:
        counter += 1
print(f'{counter} diák szövegértés pontszáma változott.')

# task 5
print('Az azonosítójuk az ellenkező irányba változott:')
for i in range(len(meres_id)):
    if sz_pont_vegleges[i] and m_pont_vegleges[i]:
        if (sz_pont_vegleges[i] > sz_pont22_23[i] and m_pont_vegleges[i] < m_pont22_23[i]) or (sz_pont_vegleges[i] < sz_pont22_23[i] and m_pont_vegleges[i] > m_pont22_23[i]):
            print(meres_id[i])
