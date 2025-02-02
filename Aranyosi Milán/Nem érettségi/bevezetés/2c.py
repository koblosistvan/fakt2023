a_oldal = float(input('Kérem adja meg a szoba hosszát méterben: '))
b_oldal = float(input('Kérem adja meg a szoba szélességét méterben: '))

sz_terulet = a_oldal * b_oldal

if sz_terulet > 30:
    print(f'Ez egy {sz_terulet} m2-es nagy szoba.')
elif 10 < sz_terulet < 30:
    print(f'Ez egy {sz_terulet} m2-es közepes szoba.')
else:
    print(f'Ez egy {sz_terulet} m2-es kis szoba.')

cs_a_oldal = float(input('Kérem adja meg a csempe hosszát: ')) / 100
cs_b_oldal = float(input('Kérem adja meg a csempe szélességét: ')) / 100
csempe_terulet = cs_a_oldal * cs_b_oldal
print(csempe_terulet)
a = sz_terulet / csempe_terulet
