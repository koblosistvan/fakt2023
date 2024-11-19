forras1 = open('top100utonev_2011.txt', 'r', encoding='utf-8')
forras2 = open('top100utonev_2021.txt', 'r', encoding='utf-8')
f11_nev = []
f11_db = []
n11_nev = []
n11_db = []
for sor in forras1:
    i = sor.strip().split('\t')
    if i[2] == 'F':
        f11_nev.append(i[0])
        f11_db.append(i[1])
    elif i[2] == 'N':
        n11_nev.append(i[0])
        n11_db.append(i[1])
forras1.close()

f21_nev = []
f21_db = []
n21_nev = []
n21_db = []
for sor in forras2:
    i = sor.strip().split('\t')
    if i[2] == 'F':
        f21_nev.append(i[0])
        f21_db.append(i[1])
    elif i[2] == 'N':
        n21_nev.append(i[0])
        n21_db.append(i[1])
forras2.close()

# 2. feladat
_2fmindkettoben = []
_2nmindkettoben = []
for i in f11_nev:
    if i in f21_nev:
        _2fmindkettoben.append(i)
for i in n11_nev:
    if i in n21_nev:
        _2nmindkettoben.append(i)
print(f'Mindkét évben szerepeltek a listákban: '
      f'{", ".join(_2fmindkettoben)}'
      f'{", ".join(_2fmindkettoben)}')
# 3. feladat
kimenet1 = open('noi_2021.txt', 'w', encoding='utf-8')
kimenet2 = open('ferfi_2021.txt', 'w', encoding='utf-8')
f21_nev_edited = f21_nev
f21_db_edited = f21_db
n21_nev_edited = n21_nev
n21_db_edited = n21_db
