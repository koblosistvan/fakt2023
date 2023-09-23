import random

PONTHATAR = 96

dolg_szama = 15  #modosithato

pontok = [random.randint(0,120) for i in range(dolg_szama)]

oszt = sum(pontok)


jeles = sum(1 for pont in pontok if pont > PONTHATAR)

haromnal_kevesebb = sum(1 for pont in pontok if pont <= 3)

tokeletes= sum(1 for pont in pontok if pont ==120)

szazalekok = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

szazalek_szeletek = [f"{szazalek}-{szazalek+9}%" for szazalek in szazalekok]

dolgozatok_szama_szeletekben = [sum(1 for pont in pontok if pont >= PONTHATAR + szazalek and pont <= PONTHATAR + szazalek + 9) for szazalek in szazalekok]

print("Pontok:")
for i, pont in enumerate(pontok):
    print(f"Dolgozat {i + 1}: {pont} pont")

for i, szazalek_szelet in enumerate(szazalek_szeletek):
    print(f"{szazalek_szelet} sáv: {dolgozatok_szama_szeletekben[i]} dolgozat")

print(f'Ebbol {jeles} db lett jeles es {haromnal_kevesebb} olyan osztalyzat volt ahol csak 3 pontnal kevesebb hianyzott, {tokeletes}db tokeletes erettsegi szuletett')
