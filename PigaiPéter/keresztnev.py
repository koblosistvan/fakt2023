source = open('PigaiPéter\\utonevek.txt', 'r', encoding='utf-8')
vezeteknev = input('>')
nevek = open('PigaiPéter\\nevek.txt', 'w', encoding='utf-8')
for i in source:
    i = i.strip('\n')
    if len(i) + len(vezeteknev) < 31:
        nevek.write('\n' + vezeteknev + ' ' + i)
    else:
        print('Nem lehetséges a 30 betűnél rövidebb név létrehozása')
source.close()
nevek.close()