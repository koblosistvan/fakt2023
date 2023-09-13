a = 5
b = 4

összeg = int(input(f'Mennyi {a} + {b} ? '))

if összeg == a + b:
    print('Ügyes vagy!')
elif abs(összeg - (a+b)) < 10:
    print('Közel vagy')
else:
    print('Jaj, már megint nem tanultál!!!')
