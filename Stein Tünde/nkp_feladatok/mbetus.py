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

nevlista = []
kezdobetu = input('Kezdőbetű: ').upper()
maxhossz = int(input('Maximális hossz: '))
nem = input('Nem: ')
eredet = input('Eredet: ')


