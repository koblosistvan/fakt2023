forras = open('utonevek.txt', 'r', encoding='utf-8')
nevek = []
for sor in forras:
    i = sor.strip().split('\n')
    nevek.append(i[0])
forras.close()
vnev = input('> ')
kimenet = []
for i in nevek:
    if len(i) <= (30-len(vnev)):
        kimenet.append(i)
print(', '.join(kimenet))