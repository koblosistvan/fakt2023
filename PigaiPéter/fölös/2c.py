a = int(input('add meg a szoba egyik hosszát:'))
b = int(input('add meg a szoba másik hosszát:'))
c = a * b
print(f'A szoba területe:{c}m^2')

#+/1
if c > 30:
    print(f'Ez egy {c}m^2-es nagy szoba')
elif 30 >= c >= 10:
    print(f'Ez egy {c}m^2-es közepes szoba')
else:
    print(f'Ez egy {c}m^2-es kis szoba')

#+/2
cs1 = int(input('add meg a csempe egyik hosszát m-be:'))
cs2 = int(input('add meg a csempe egyik hosszát m-be:'))
cs1a = a / cs1
cs1b = b / cs1
cs2a = a / cs2
cs2b = b / cs2

if cs1a.is_integer() == True and cs2b.is_integer() == True or cs1b.is_integer() == True and cs2a.is_integer() == True:
    print(f'{int(cs1a + cs2b)}db csempére lesz szükség')
    csveszt = (cs1a * cs2b) + (cs1a * cs2b) / 100 * 10
    csossz = cs1a * cs2b + csveszt
elif cs1b.is_integer() == True and cs2a.is_integer() == True:
     print(f'{int(cs2a + cs1b)}db csempére lesz szükség')
     csveszt = (cs2a * cs1b) + (cs2a * cs1b) / 100 * 10
     csossz = cs2a * cs1b + csveszt
elif cs1a.is_integer() == True and cs2b.is_integer() == True and cs1b.is_integer() == True and cs2a.is_integer() == True:
     print(f'{int(cs2a + cs1b)}db csempére lesz szükség')
     csveszt = (cs1a * cs2b) + (cs1a * cs2b) / 100 * 10
     csossz = cs1a * cs2b + csveszt
else:
    print('nem lehet leburkolni egész csempékből')

#+3
import math
doboz = math.ceil(csossz / 12)
print(f'{doboz} doboz csempét kell berendelni')




