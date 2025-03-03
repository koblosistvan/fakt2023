source = open('PigaiPéter\\dallista.txt', 'r', encoding='utf-8')
maffia = open('PigaiPéter\\maffia.txt', 'w', encoding='utf-8')
időpont = []
előadó = []
cím = []
for elem in source:
    elem = elem.strip().split('\t')
    időpont.append(elem[0])
    előadó.append(elem[1])
    cím.append(elem[2])
for i in range(len(előadó)):
    if előadó[i] == 'Irie Maffia':
        maffia.write(időpont[i] + cím[i] + '\n')