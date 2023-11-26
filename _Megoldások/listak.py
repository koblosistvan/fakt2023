gyümölcsök = ['alma', 'körte', 'banán', 'cseresznye', 'meggy', 'füge']

print(gyümölcsök)
print(gyümölcsök[0])
print(gyümölcsök[2:4])
print(gyümölcsök[2:])
print(gyümölcsök[:3])
print(gyümölcsök[-4])
print(gyümölcsök[-3:])
print(len(gyümölcsök))

gyümölcsök[0] = 'szilva'
gyümölcsök.append('alma')
print(gyümölcsök)

print("hello, Manu".split())

lista = [2,5,7,23,6,33,2,5,6,3,2,1]
adat = [int(a) for a in sor.strip().split(' ')]
egyész = [int(a) for a in lista[:3]]
szűrt = [a*10 for a in lista if a > 5]
print(szűrt)
#nagyobb30 = [h for h in hőmérséklet if h > 30]
nőtt = len([i for i in range(len(lista)-1) if lista[i] < lista[i+1]])

szülinap = [int(a) for a in input('Add meg a szülinapodat: ').split(' ')]
szülinap = [2007, 1, 26]