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
      f'\n{", ".join(_2fmindkettoben)}'
      f'\n{", ".join(_2nmindkettoben)}')
# 3. feladat
kimenet1 = open('ferfi_2021.txt', 'w', encoding='utf-8')
kimenet2 = open('noi_2021.txt', 'w', encoding='utf-8')
f21_nev_edited = f21_nev
f21_db_edited = f21_db
n21_nev_edited = n21_nev
n21_db_edited = n21_db
for i in range(len(f21_nev_edited)-1):
    if f21_db_edited[i] < f21_db_edited[i+1]:
        f21_db_edited[i], f21_db_edited[i+1] = f21_db_edited[i+1], f21_db_edited[i]
        f21_nev_edited[i], f21_nev_edited[i + 1] = f21_nev_edited[i + 1], f21_nev_edited[i]
for i in f21_nev_edited:
    print(i, file=kimenet1)
for i in range(len(n21_nev_edited)-1):
    if n21_db_edited[i] < n21_db_edited[i+1]:
        n21_db_edited[i], n21_db_edited[i+1] = n21_db_edited[i+1], n21_db_edited[i]
        n21_nev_edited[i], n21_nev_edited[i + 1] = n21_nev_edited[i + 1], n21_nev_edited[i]
for i in n21_nev_edited:
    print(i, file=kimenet2)

# 4. feladat
kimenet3 = open('noinevekmozgasa.txt', 'w', encoding='utf-8')
n11_nev_edited = n11_nev
n11_db_edited = n11_db
for i in range(len(n11_nev_edited)-1):
    if n11_db_edited[i] < n11_db_edited[i+1]:
        n11_db_edited[i], n11_db_edited[i+1] = n11_db_edited[i+1], n11_db_edited[i]
        n11_nev_edited[i], n11_nev_edited[i + 1] = n11_nev_edited[i + 1], n11_nev_edited[i]
for i in n11_nev_edited:
    if i in n21_nev_edited:
        print(f'{i}\t{n11_nev_edited.index(i)+1}\t{n21_nev_edited.index(i)+1}'
              f'\t{n11_nev_edited.index(i)-n21_nev_edited.index(i)}', file=kimenet3)
