forras = open('tavirathu13.txt', mode='r', encoding='utf-8')

telepules = []
ido = []
szelirany_es_erosseg = []
homerseklet = []

for sor in forras:
    adat = sor.strip().split(' ')
    telepules.append(adat[0])
    ido.append(int(adat[1]))
    szelirany_es_erosseg.append(adat[2])
    homerseklet.append(int(adat[3]))



forras.close()

print(ora)
print(perc)
varos = input('Adja meg egy település kódját! Település: ')
for i in reversed(telepules):
    if telepules == varos:
        print(f'Az utolsó mérési adat a megadott településről {ido}-kor érkezett. ')
        break

legalacsonyabb = homerseklet[0]
alacsony_id = 0
legmagasabb = homerseklet[0]
magas_id = 0
for i in range(len(telepules)):
    if homerseklet[i] < legalacsonyabb:
        legalacsonyabb = homerseklet[i]
        alacsony_id = i
    elif homerseklet[i] > legmagasabb:
        legmagasabb = homerseklet[i]
        magas_id = i
print(f'A legalacsonyabb hőmérséklet: {telepules[alacsony_id]} {ido[alacsony_id]} {legalacsonyabb} fok.\nA legmagasabb hőmérséklet: {telepules[magas_id]} {ido[magas_id]} {legalacsonyabb} fok.')

szamlalo = 0
for i in range(len(telepules)):
    if szelirany_es_erosseg == '00000':
        print(f'{telepules[i]} {ido[i]}')
        szamlalo += 1
if szamlalo == 0:
    print('Nem volt szélcsend a mérések idején.')

