forras = open('utonevek.txt', 'r', encoding='utf-8')
vnev = input('> ')
nevek = []
magas = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű',
         'E', 'É', 'I', 'Í', 'Ö', 'Ő', 'Ü', 'Ű']
mely = ['a', 'á', 'o', 'ó', 'u', 'ú',
        'A', 'Á', 'O', 'Ó', 'U', 'Ú']
kimenet = []
for sor in forras:
    i = sor.strip().split()
    nevek.append(i[0])
forras.close()


def hangrend(x):
    amagas = False
    amely = False
    for i in x:
        if i in magas:
            amagas = True
        if i in mely:
            amely = True
    if amagas and amely:
        melyik = 'vegyes'
    elif amagas:
        melyik = 'magas'
    else:
        melyik = 'mely'
    return melyik


for i in nevek:
    if hangrend(i) == hangrend(vnev):
        kimenet.append(i)
print(', '.join(kimenet))
