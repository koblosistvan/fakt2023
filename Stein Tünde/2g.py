a = int(input('Add meg az "a" számot: '))
b= int(input('Add meg a "b" számot: '))

if a % b == 0 or b % a ==0:
    print('Az "a" szám és a "b" szám oszthatóak egymással valahogy')
else:
    print('Az "a" szám és a "b" szám nem oszthatóak egymással')