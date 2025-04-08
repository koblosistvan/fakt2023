bemenet = input('Kérem a TAJ-számot: ')
tajszam = []
for i in bemenet:
    tajszam.append(int(i))
szorzat = 0
for i in range(len(tajszam)-1):
    if (i+1) % 2 != 0:
        szorzat += 3 * tajszam[i]
    else:
        szorzat += 7 * tajszam[i]
print(f'Az ellenőrzőszámjegy: {tajszam[-1]}\nA szorzatok összege: {szorzat}')
if szorzat % 10 == tajszam[-1]:
    print(f'Helyes a szám!')
else:
    print(f'Hibás a szám!')
