kerubina = [sor.strip() for sor in open('Kerubina.txt', mode='r', encoding='utf-8')]
triton = [sor.strip() for sor in open('Triton.txt', mode='r', encoding='utf-8')]

# Metszet
metszet = []
for film in kerubina:
    if film in triton:
        metszet.append(film)
print('-'*50, '\nNyers szöveg')
print('\n'.join(metszet))

# Advanced megoldás
metszet = set(kerubina).intersection(set(triton))
print('-'*50, '\nNyers szöveg')
print('\n'.join(metszet))


# Únió
únió = kerubina.copy()
for film in triton:
    if film not in únió:
        únió.append(film)
print('-'*50, '\nNyers szöveg')
print('\n'.join(únió))

# hogy lehet elfontani?
print(len(kerubina))
únió = kerubina
for film in triton:
    if not film in únió:
        únió.append(film)
print(len(kerubina))
# akkor csináljuk vissza...
kerubina = [sor.strip() for sor in open('Kerubina.txt', mode='r', encoding='utf-8')]

'''
# hogy lehet elfontani II?
únió = kerubina.copy
for film in triton:
    if not film in únió:
        únió.append(film)
'''

# Advanced megoldás
únió = set(kerubina).union(set(triton))
únió = set(kerubina + triton)
print('Vége.')


print(sorted('anna') == sorted('na'))