forrás = open('kocka.graf', mode='r')

gráf = []
for sor in forrás:
    adat = sor.strip().split('\t')
    gráf.append(adat)
forrás.close()

# 3 6 1 5
útvonal = input('Merre szeretnél menni? ').split(' ')
for i in range(len(útvonal)-1):
    keresett_él = [útvonal[i], útvonal[i+1]]
    if keresett_él not in gráf:
        print(f'Ez sajnos nem járható be, {"->".join(keresett_él)} él nincs.')
        break
else:
    print('Tuti, ez bejárható!!!')

