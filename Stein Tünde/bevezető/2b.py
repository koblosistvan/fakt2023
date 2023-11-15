a_szám = 35
b_szám = 753489
összeg = int(input('Mennyi a két szám összege? '))

if összeg == a_szám + b_szám:
    print('Igen.')
elif abs(összeg - a_szám + b_szám < 1000 ):
    print('Közel.')
else:
    print('Nem.')