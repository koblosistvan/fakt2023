forras = open('utonevek.txt', 'r', encoding='utf-8')
vnev = input('> ')
nevek = []
magas = [e, é, i, í, ö, ő, ü, ű]
mely = [a, á, o, ó, u, ú]
for sor in forras:
    i = sor.strip().split()
    nevek.append(i[0])
forras.close()
melyik = 3
for i in vnev:
    if i not in magas:
        melyik = 2
    if i not in mely:
        melyik = 1
for i in nevek:
