# 1. 
melyseg = [int(sor.strip()) for sor in open("Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_21maj/e_inffor_21maj_fl/4_Godrok/melyseg.txt",'r',encoding="utf-8")]
print("1. feladat\nA fájl adatainak száma:",len(melyseg))

# 2. 
print("\n2. feladat")
prompt = int(input("Adjon meg egy távolságértéket! ").strip()) -1
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
print("\n5. feladat\nA gödrök száma:",len(godrok))

# 6. 

def get_godor(p:int)->int: # godor indexet adja vissza
    if not melyseg[p]:
        return None
    else:
        for i in range(len(godrok)):
            if godrok_indexek[i] <= p <= godrok_indexek[i] + len(godrok[i]):
                return i
        return None
            

print("\n6. feladat")
def menet()->bool:
    godor = godrok[prompt]
    irany_le = True # igaz, ha lefele tesztel, hamis ha felfele
    for i in range(len(godor)-1):
        if irany_le:
            if godor[i] < godor[i+1]: # nem volt irva hogy szigoruan monoton
                return False
        else:
            if godor[i] > godor[i+1]:
                return False
    return True

prompt = get_godor(prompt)

if None == prompt:
    print("Az adott helyen nincs gödör.")
else:
    # a)
    print(f"a)\nA gödör kezdete: {godrok_indexek[prompt]+1} méter, a gödör vége: {godrok_indexek[prompt]+len(godrok[prompt])} méter.")
    # b)
    print("b)\n" + ("Folyamatosan mélyül." if menet() else "Nem mélyül folyamatosan."))
    # c)
    print(f"c)\nA legnagyobb mélysége {max(godrok[prompt])} méter.")
    # d)
    print("d)\nA térfogata",sum([10*i for i in godrok[prompt]]),"m^3.")
    # e)
    print("e)\nA vízmennyiség",sum([10*(i-1) for i in godrok[prompt]]),"m^3.")
