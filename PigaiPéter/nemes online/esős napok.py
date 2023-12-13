forras = open('esos.txt', mode='r', encoding='utf-8')
forras.read()
mm = []
for sor in forras:
    mm.append(sor.strip().split(' '))
print(mm)