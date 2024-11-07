source = open('PigaiPéter\\utonevek.txt', 'r', encoding='utf-8')
vezeteknev = input('>')
nevek = open('PigaiPéter\\nevek.txt', 'w', encoding='utf-8')
magas = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
mély = ['a', 'á', 'o', 'ó', 'u', 'ú' ]
vma_counter = 0
vmé_counter = 0
for betű in vezeteknev:
    if betű in magas:
        vma_counter += 1
    elif betű in mély:
        vmé_counter += 1
    for név in source:
        név = név.strip('\n')
        kma_counter = 0
        kmé_counter = 0
        for betű in név:
            betű = betű.lower()
            if betű in magas:
                kma_counter += 1
            elif betű in mély:
                kmé_counter += 1
        if kma_counter > 0 and kmé_counter == 0 and vma_counter > 0 and vmé_counter == 0:
            nevek.write('\n' + vezeteknev + " " + név)
        elif vma_counter == 0 and vmé_counter > 0 and kma_counter == 0 and kmé_counter > 0:
            nevek.write('\n' + vezeteknev + ' ' + név)
        elif vma_counter > 0 and vmé_counter > 0 and kma_counter > 0 and kmé_counter > 0:
            nevek.write('\n' + vezeteknev + ' ' + név)
source.close()
nevek.close()