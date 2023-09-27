szam = int(input('Szám: '))
a = True
if szam <= 1:
    print(f'{szam} nem egy prímszám.')
elif szam > 1:
    for i in range(2, szam):
        if szam % i == 0:
            a = False
            break
if a is False:
    print(f'{szam} nem egy prímszám.')
else:
    print(f'{szam} prímszám.')
