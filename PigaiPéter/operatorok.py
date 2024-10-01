class Operatorok:
    def __init__(self, elso:int, operator:str, masodik:int):
        self.elso = elso
        self.operator = operator
        self.masodik =masodik
forras = open('PigaiPéter\\operatorok.txt', mode='r', encoding='utf-8')
data =[]
for i in forras:
    sor = i.strip().split(' ')
    data.append(Operatorok(elso=int(sor[0]), operator=str(sor[1]), masodik=int(sor[2])))
forras.close()

#
print(f'2.feladat: kifejezések száma {len(data)}')

#
mod = 0
for i in data:
    if i.operator == 'mod':
        mod += 1
print(f'3.feladat: kifejezések maradékos osztással {mod}')

#
van = False
for i in data:
    if i.elso % 10 == 0 and i.masodik % 10 == 0:
        van = True
        break
if van:
    print('4.feladat: Van ilyen kifejezés')
else:
    print('4.feladat: Nincs ilyen kifejezés')

#
print('5.feladat: Statisztika')
muveletfajtak = {'+', '-', '*', '/', 'div', 'mod'}
muveletek = []
for i in data:
    muveletek.append(i.operator)
for i in muveletfajtak:
    print(f'\t{i} -> {muveletek.count(i)} db')

#
def muvelet(a, b, c):
    a = int(a)
    c = int(c)
    if b == '+':
        return()