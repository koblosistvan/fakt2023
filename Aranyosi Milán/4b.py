import random

HATAR = 96
pontszamok = []
jelesdb = 0
majdnemotos = 0
maxdb = 0
savok = {
    '0-10': 0,
    '10-20': 0,
    '20-30': 0,
    '30-40': 0,
    '40-50': 0,
    '50-60': 0,
    '60-70': 0,
    '70-80': 0,
    '80-90': 0,
    '90-100': 0
}

def savfgv(p):
    szazalek = p/120*100
    if szazalek < 10:
        savok['0-10'] += 1
    elif szazalek < 20:
        savok['10-20'] += 1
    elif szazalek < 30:
        savok['20-30'] += 1
    elif szazalek < 40:
        savok['30-40'] += 1
    elif szazalek < 50:
        savok['40-50'] += 1
    elif szazalek < 60:
        savok['50-60'] += 1
    elif szazalek < 70:
        savok['60-70'] += 1
    elif szazalek < 80:
        savok['70-80'] += 1
    elif szazalek < 90:
        savok['80-90'] += 1
    else:
        savok['90-100'] += 1

for i in range(100):
    pontszamok.append(random.randint(0, 120))
    if pontszamok[i] >= 96:
        jelesdb += 1
    if pontszamok[i] >= 93 and pontszamok[i] < 96:
        majdnemotos += 1
    if pontszamok[i] == 120:
        maxdb += 1
    savfgv(pontszamok[i])

for x in range(len(savok)):
    print(str(list(savok.keys())[x]) + ": " + str(list(savok.values())[x]))

print(f'{sum(pontszamok)/100} a számok átlaga.')

print(f'{jelesdb} jeles született.')

print(f'{majdnemotos} darabhoz kellett volna 3 pont vagy kevesebb az ötöshöz.')
