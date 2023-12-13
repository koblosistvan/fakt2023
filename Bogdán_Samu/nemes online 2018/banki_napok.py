forrás = open('banki napok.txt')
x = forrás.readline()
aznosító = []
belépés_napja = []
for i in forrás:
    aznosító.append(int(i.strip().split(' ')[0]))
    belépés_napja.append(int(i.strip().split(' ')[1]))

print(f'a. feladat')
print(aznosító.count(1), aznosító.count(2))
