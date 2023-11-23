def kinyert(pakli, húzások):
    a = 0
    b = 0
    for i in range(len(pakli)):
        if húzások[i] == 'A':
            a += int(pakli[i])
        else:
            b += int(pakli[i])
    if b > 21 or (a <= 21 and a > b):
        return f'A lapjainak összege {a}, B lapjainak összege {b}, tehát A nyert.'
    elif a > 21 or (b <= 21 and b > a):
        return f'A lapjainak összege {a}, B lapjainak összege {b}, tehát B nyert.'

pakli = list(input('Pakli: ').split(','))
húzások = list(input('Húzások: ').split(','))
print(kinyert(pakli, húzások))
