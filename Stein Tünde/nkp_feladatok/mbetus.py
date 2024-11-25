forras1 = open('noi_nevek_eredete.txt', 'r', encoding='utf-8')
forras2 = open('ferfi_nevek_eredete.txt', 'r', encoding='utf-8')
noinevek = []
n_eredet = []
ferfinevek = []
f_eredet = []
for sor in forras1:
    i = sor.strip().split(',')
    noinevek.append(i[0])
    n_eredet.append(i[1])
forras1.close()
for sor in forras2:
    i = sor.strip().split(',')
    ferfinevek.append(i[0])
    f_eredet.append(i[1])
forras2.close()

lista = []
kbetu = input('Kezdőbetű: ').upper()
maxh = int(input('Maximális hossz: '))
neme = input('Nem: ')
eredete = input('Eredet: ')


def NevKivalaszt(nevlista, kezdobetu, maxhossz, nem, eredet):
    if nem in ('férfi', 'Férfi', 'ferfi', 'Ferfi'):
        for i in range(len(ferfinevek)):
            if ferfinevek[i][0] == kezdobetu and len(ferfinevek[i]) <= maxhossz and eredet in f_eredet[i].split('-'):
                nevlista.append(ferfinevek[i])
    elif nem in ('nő', 'Nő', 'no', 'No'):
        for i in range(len(noinevek)):
            if noinevek[i][0] == kezdobetu and len(noinevek[i]) <= maxhossz and eredet in n_eredet[i].split('-'):
                nevlista.append(noinevek[i])
    return nevlista


print(', '.join(NevKivalaszt(lista, kbetu, maxh, neme, eredete)))
