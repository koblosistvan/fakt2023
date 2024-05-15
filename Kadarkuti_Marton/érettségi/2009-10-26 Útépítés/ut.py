# 0.
def vonal():
    print("-"*30)

idopont = []
athaladas = []
irany = []

def masodperc(h,m,s):
    return 3600*h + 60*m + s

with open("forgalom.txt","r",encoding="utf-8") as f:
    f.readline()
    for sor in f:
        adat = sor.strip().split(" ")
        adat = list( map( int, adat[:4] ) ) + list(adat[4])

        idopont.append( masodperc( adat[0],adat[1],adat[2] ) )
        athaladas.append( adat[3] )
        irany.append( adat[4] )

# 1.
while True:
    vonal()
    try:
        nEdikInput = int(input("> "))
        if irany[nEdikInput] == "F":
            print(f"{nEdikInput}. belépő jármű a felső város felé haladt.")
        else:
            print(f"{nEdikInput}. belépő jármű az alsó város felé haladt.")
        vonal()
        break
    except:
        vonal()
        print("Érvénytelen bemenet.")

# 2.
utolsoKetto = []
i = -1
while len(utolsoKetto) < 2:
    if irany[i] == "F":
        utolsoKetto.append( idopont[i] )
    i -= 1
del i
utolsoKettoOutput = abs( utolsoKetto[0] - utolsoKetto[1] )
print(f"Az utolsó kettő felfelé tartó jármű {utolsoKettoOutput}s különbséggel érte el az útszakasz kezdetét.")
vonal()

# 3.
    ### ROSSZ
orankent = [0]*10  # 7:00 - 16:00
also_es_felso = [0]*2
for i in range(len(idopont)):
    orankent[ idopont[i]//3600 -1 ] += 1
    if irany[i] == "A":
        also_es_felso[0] += 1
    else:
        also_es_felso[1] += 1
for i in range(len(orankent)):
    print(f"{i+1}. órában {orankent[i]} autó haladt el.")
print(f"{also_es_felso[0]} alsó,")
print(f"{also_es_felso[1]} felső.")