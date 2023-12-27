forrás = open('kerekparverseny.txt', mode='r')
x = forrás.readline().strip()
városok = int(x.split(' ')[0])
hossz = int(x.split(' ')[1])
táv = []
for i in forrás:
    táv.append(int(i.strip()))
km = 0
lezárandó = 0
id2 = 1
for i in range(len(táv)):
    if táv[i] < hossz:
        km += táv[i]
        lezárandó += 1
        if km == hossz:
            break
    elif táv[i] == hossz:
        print()
print()