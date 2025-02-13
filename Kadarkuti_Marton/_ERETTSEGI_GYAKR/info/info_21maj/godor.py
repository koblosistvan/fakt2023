# 1. 
melyseg = [int(sor.strip()) for sor in open("Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_21maj/e_inffor_21maj_fl/4_Godrok/melyseg.txt",'r',encoding="utf-8")]
print("1. feladat\nA fájl adatainak száma:",len(melyseg))

# 2. 
print("\n2. feladat")
prompt = 8#int(input("Adjon meg egy távolságértéket! ").strip()) -1
print(f"Ezen a helyen a felszín {melyseg[prompt]} méter mélyen van. ")

# 3. 
print("\n3. feladat")
print(f"Az érintetlen terület aránya {(melyseg.count(0)/len(melyseg)):.2%}. ")

# 4. 
godrok:list[list[int]] = [[]]
godrok_indexek = []

# az i. godor:
#  kezdopontja godrok_indexek[i], hossza len(godrok[i]), ertekei godrok[i]

uj_sor = False
for i in range(len(melyseg)):
    if melyseg[i]:
        godrok[-1].append(melyseg[i])
    else:
        if len(godrok[-1]):
            godrok_indexek.append(i - len(godrok[-1]))
            godrok.append([])

if not godrok[-1]:
    godrok = godrok[:-1]
    godrok_indexek = godrok_indexek[:-1]

with open("Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_21maj/godrok.txt",'w',encoding="utf-8") as x:
    for sor in godrok:
        x.write(' '.join(map(str,sor)) + '\n')

# 5. 
print(godrok)
print(godrok_indexek)
print("\n5. feladat\nA gödrök száma:",len(godrok))

# 6. 

def get_godor(prompt:int)->list[int]:
    ki = []
    if not melyseg[prompt]:
        return ki
    else:
        pass

print("\n6. feladat")
prompt = get_godor(prompt)
if not prompt:
    print("Az adott helyen nincs gödör.")
else:
    # a)
    pass

"""""""""""""""""""""""""""
6. feladat
a)
A gödör kezdete: 7 méter, a gödör vége: 22 méter.
b)
Nem mélyül folyamatosan.
c)
A legnagyobb mélysége 4 méter.
d)
A térfogata 440 m^3.
e)
A vízmennyiség 280 m^3. 
"""""""""""""""""""""""""""
