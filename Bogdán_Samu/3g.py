import random

kő = "kő"
papír = "papír"
olló = "olló"
pontg = 0
pontj = 0
opt = [kő, papír, olló]

print("Első forduló.")
jatekos = str(input("Kő, papír vagy olló: "))
gep = random.choice(opt)   # todo: random.choice
if jatekos == gep:
    print("Döntetlen.")
elif jatekos == kő and gep == papír:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == kő and gep == olló:
    pontj = pontj + 1
    print("Ön nyert.")
elif jatekos == papír and gep == kő:
    pontj = pontj + 1
    print("Ön nyert.")
elif jatekos == papír and gep == olló:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == olló and gep == kő:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == olló and gep == papír:
    pontj = pontj + 1
    print("Ön nyert.")
else:
    str(input("Nem értem. Kő, papír vagy olló: "))

print("Második forduló.") # todo: ezt ciklussal kell
jatekos = str(input("Kő, papír vagy olló: "))
gep = random.choice(opt)
if jatekos == gep:
    print("Döntetlen.")
elif jatekos == kő and gep == papír:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == kő and gep == olló:
    pontj = pontj + 1
    print("Ön nyert.")
elif jatekos == papír and gep == kő:
    pontj = pontj + 1
    print("Ön nyert.")
elif jatekos == papír and gep == olló:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == olló and gep == kő:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == olló and gep == papír:
    pontj = pontj + 1
    print("Ön nyert.")
else:
    str(input("Nem értem. Kő, papír vagy olló: "))

print("Harmadik forduló.")
jatekos = str(input("Kő, papír vagy olló: "))
gep = random.choice(opt)
if jatekos == gep:
    print("Döntetlen.")
elif jatekos == kő and gep == papír:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == kő and gep == olló:
    pontj = pontj + 1
    print("Ön nyert.")
elif jatekos == papír and gep == kő:
    pontj = pontj + 1
    print("Ön nyert.")
elif jatekos == papír and gep == olló:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == olló and gep == kő:
    pontg = pontg + 1
    print("Ön vesztett.")
elif jatekos == olló and gep == papír:
    pontj = pontj + 1
    print("Ön nyert.")
else:
    str(input("Nem értem. Kő, papír vagy olló: "))

