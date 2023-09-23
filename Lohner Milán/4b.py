import random

PONTHATAR = 96

dolg_szama = 15  #modosithato

pontok=[random.randint(0,120) for i in range(dolg_szama)]

oszt=sum(pontok)
print(pontok,'ilyen eredmenyek szulettek')


jeles = sum(1 for pont in pontok if pont > PONTHATAR)

haromnal_kevesebb = sum(1 for pont in pontok if pont <= 3)

tokeletes= sum(1 for pont in pontok if pont ==120)

print(f'Ebbol {jeles} db lett jeles es {haromnal_kevesebb} olyan osztalyzat volt ahol csak 3 pontnal kevesebb hianyzott, {tokeletes}db tokeletes erettsegi szuletett')



