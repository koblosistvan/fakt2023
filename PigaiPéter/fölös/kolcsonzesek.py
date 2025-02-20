class Kolcsonzes:
    def __init__(self, nev: str, jid: str, eora: int, eperc: int, vora: int, vperc: int):
        self.nev = nev
        self.jid = jid
        self.eora = eora
        self.eperc = eperc
        self.vora = vora
        self.vperc = vperc

forras = open('PigaiPéter\\kolcsonzesek.txt', 'r', encoding='utf-8')
forras.readline()
data = []
for i in forras:
    i = i.strip().split(';')
    data.append(Kolcsonzes(nev=str(i[0]), jid=str(i[1]), eora=int(i[2]), eperc=int(i[3]), vora=int(i[4]), vperc=(i[5])))
forras.close()

#5
print('5. feladat:')
print(f'{len(data)}')

#6
kertnev = input('Név:')
for i in range(len(data)):
    if data[i].nev == kertnev:
        print(f'{"0" + str(data[i].eora) if (int(data[i].eora) < 10) else data[i].eora}:{"0" + str(data[i].eperc) if (int(data[i].eperc) < 10) else data[i].eperc}-{"0" + str(data[i].vora) if (int(data[i].vora) < 10) else data[i].vora}:{"0" + str(data[i].vperc) if (int(data[i].vperc) < 10) else data[i].vperc}')
    else:
        print('Nem volt ilyen nevű kölcsönző')

#7
