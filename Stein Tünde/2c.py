# kicsit hiányos


a = int(input('Add meg a szoba szélességét: '))
b = int(input('Add meg a szoba hosszúságát: '))

if a*b > 30:
    m = 'nagy'
elif a*b > 10:
    m = 'közepes'
else:
    m = 'kis'
print(f'Ez egy {a*b} m2-es {m} szoba.')

c = int(input('Add meg a csempe szélességét: '))
d = int(input('Add meg a csempe hosszúságát: '))
cs = (a*b)/(c*d)

if (a % c == 0 and b % d == 0) or (b % c == 0 and a % d == 0):
    print(f'A szoba burkolható a csempékkel. {round(cs)} csempe kell hozzá.')
else:
    print('A szoba nem burkolható a csempékkel maradéktalanul.')

print(f'A 10% veszteséggel együtt {round(cs*1.1)} csempére van szükség, ami {round(cs/12)+1} doboz csempének felel meg.')