forras1 = open('triton.txt', 'r', encoding='utf-8')
forras2 = open('kerubina.txt', 'r', encoding='utf-8')
triton = []
kerubina = []
unio = []
for sor in forras1:
    i = sor.strip()
    triton.append(i)
forras1.close()
for sor in forras2:
    i = sor.strip()
    kerubina.append(i)
forras2.close()
for i in triton:
    if i in kerubina and i not in unio:
        unio.append(i)
print(unio)
