import random

érettségi_pontok = []
jeles = 0
majdnem_jeles = 0
max = 0
Ponthatár = 96

for i in range(100):
    érettségi_pontok.append(random.randint(0, 120))
for i in range(len(érettségi_pontok)):
    if érettségi_pontok[i] >= Ponthatár:
        if érettségi_pontok[i] == 120:
            max += 1
        else:
            jeles += 1
    elif Ponthatár > érettségi_pontok[i] > Ponthatár - 3:
        majdnem_jeles += 1
összpontok = 0
for i in range(100):
    összpontok += érettségi_pontok[i]
print(f'Érettségi pontok: {érettségi_pontok}.\nJelesek száma: {jeles}.\n{majdnem_jeles} alkalommal múlt kevesebb mint 3 ponton.\n{max} maximum pontos lett.\nA pontok átlaga: {összpontok/len(érettségi_pontok)}.')

_10 = 0
_20 = 0
_30 = 0
_40 = 0
_50 = 0
_60 = 0
_70 = 0
_80 = 0
_90 = 0
_100 = 0
for i in range(100):
    if érettségi_pontok[i] <= 120 * 0.1:
        _10 += 1
    elif érettségi_pontok[i] <= 120 * 0.2:
        _20 += 1
    elif érettségi_pontok[i] <= 120 * 0.3:
        _30 += 1
    elif érettségi_pontok[i] <= 120 * 0.4:
        _40 += 1
    elif érettségi_pontok[i] <= 120 * 0.5:
        _50 += 1
    elif érettségi_pontok[i] <= 120 * 0.6:
        _60 += 1
    elif érettségi_pontok[i] <= 120 * 0.7:
        _70 += 1
    elif érettségi_pontok[i] <= 120 * 0.8:
        _80 += 1
    elif érettségi_pontok[i] <= 120 * 0.9:
        _90 += 1
    else:
        _100 += 1
print(f'10% alatt: {_10}, 20% alatt: {_20}, 30% alatt: {_30}, 40% alatt: {_40}, 50% alatt: {_50},\n60% alatt: {_60}, 70% alatt: {_70}, 80% alatt: {_80}, 90% alatt: {_90}, 90% felett: {_100}')
