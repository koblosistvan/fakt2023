napok_száma = input('Napok száma: ')
csapadék_adatok = input('Csapadék: ')
# 11
# 5 0 0 0 0 5 0 3 3 0 0

csapadék = []
for napi in csapadék_adatok.split(' '):
    csapadék.append(int(napi))

print('a. feladat')
esett = 0
for i in range(len(csapadék)):
    if csapadék[i] > 0:
        esett += 1
print(f'{esett} napon esett az eső.')


print('\nb. feladat')
száraz = 0
def száraz_napo_száma(kezdő_nap):
    nap_sorszáma = kezdő_nap
    while nap_sorszáma < len(csapadék) and csapadék[nap_sorszáma] == 0:
        nap_sorszáma += 1
    return nap_sorszáma - kezdő_nap

for i in range(len(csapadék)):
    if száraz_napo_száma(i) > száraz_napo_száma(száraz):
        száraz = i
print(f'A leghosszabb csapadékmentes időszak {száraz_napo_száma(száraz)} napig tartott')

print('\nc. feladat')
két_nap_max_id = 0
for i in range(1, len(csapadék)-1):
    if csapadék[i] + csapadék[i+1] > csapadék[két_nap_max_id] + csapadék[két_nap_max_id+1]:
        két_nap_max_id = i
print(f'Két nap alatt leesett legtöbb csapadék {csapadék[két_nap_max_id] + csapadék[két_nap_max_id+1]} mm volt.')

'''
d.
Írj programot, amely megadja a leghosszabb intervallumot, amelyen belül a napok legalább felében esett az eső, valamint az intervallum első és utolsó napján is esett! Írd ki az első és utolsó nap sorszámát!
print(csapadék)

'''
