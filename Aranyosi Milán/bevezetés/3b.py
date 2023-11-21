print('Mettől meddig irja ki a program a számokat?')
a = int(input('Ettől:'))
b = int(input('Eddig:'))

for i in range(a, b + 1):
    print(i)