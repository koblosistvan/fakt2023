def vonal():
    print("-"*30)

# KöMaL 2023 december, I603. feladat
# I. BEMENET
validUserInput = False
print("Adj meg két számot <szóközzel> elválasztva!")
while True:
    try:
        vonal()
        listUserInput = list(map(int, (input("[>] ").strip().split(" "))))
        #print(listUserInput)
        if len(listUserInput) > 2:
            raise()
        a,b = listUserInput[0], listUserInput[1]  # elmentett bemenet
        if a < b:
            a,b=b,a
        break
    except:
        print("Érvénytelen bemenet.")

# II. BEMENET FELDOLGOZÁSA

# a program szétbontja a két bemeneti számot minden számunkra érdekes tübbjegyű komponensre,
# és ezt elmenti az ahhoz tartozó listába (sub_n , sub_b)
# pl: ha a=345, akkor sub_a=[3,4,5,34,45,345] (ez lesz a sublist(n) függvény)
# a nullával kezdődő komponensek érvénytelenek,
# pl: a=1001, akkor abból a "00","01","001" részek érvénytelenek,
    # viszont a nulla mint számjegy annyiszor érvényes, ahányszor szerepel

def join(lista):  # pl: [1,2,3] => 123
    if lista[0] == 0 and len(lista) > 1: # nullával kezdődő részek érvénytelenítése
        return None   # az indexeltség miatt helyettesítő érték kell
    lista = "".join( map(str,lista))
    return int(lista)

def sublist(n):
    n = list( map(int, list(str(n))) )  # 123 => [1,2,3]
    r = []       # return érték
    for i in range(len(n)):
        for j in range(1 + i, len(n) + 1):
            r.append( join( n[i:j] ) )

    for i in range(r.count(None)): # helyettesítő értékek eltávolítása
        r.remove(None)
    return sorted(r)

sub_a, sub_b = sublist(a), sublist(b)
#print(sub_a,sub_b)

# III. SZÁMÍTÁS

# d: "divisibility" függvény
# return értékek:
    # 1, ha a|b
    # 0, ha a∤b, ha b=0, vagy ha b nem egyjegyű,
                        # mert a példa alapján az osztó mindig egy számjegy

def d(a,b):
    if len(str(b)) > 1:  # számjegyek száma nagyobb egynél
        return 0
    if b == 0: # zéróosztó
        return 0
    if a%b == 0:
        return 1
    return 0

# a végeredmény ("szimpátia") számítása:
    # a két lista minden két-két elemének egymással való oszthatóságát
    # teszteljük a d() függvénnyel, ezeknek összege a kimenet

# a két lista tesztelése ugyanaz a kód, ezért függvényként egyszerűbb
def mindent_leoszt(lista_a, lista_b):
    szimpatiaReturnErtek = 0
    for i in range( len(lista_a) ):
        for j in range( len(lista_b) ):

            ai, bj = lista_a[i], lista_b[j] # átláthatóbb
            szimpatiaReturnErtek += d(ai, bj)

            #print(f"{ai},{bj} ={d(ai, bj)}")
    return szimpatiaReturnErtek

# kimeneti érték:
szimpatiaOutput = mindent_leoszt(sub_a, sub_b) + mindent_leoszt(sub_b, sub_a)

# IV. KIMENET
vonal()
print(f"{a} és {b} számok szimpátiája: {szimpatiaOutput} ")
vonal()
