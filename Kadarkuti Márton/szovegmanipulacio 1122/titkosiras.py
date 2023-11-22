MAGYAR = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"
CYPHER = "öüóűqwertzuiopőúasdfghjkléáíyxcvbnm"

def kodol_dekodol(szo, kodole):
    output = [i for i in szo]

    if kodole:
        for i in range(len(szo)):
            output[i] = MAGYAR[CYPHER.index(szo[i])]
    else:
        for i in range(len(szo)):
            output[i] = CYPHER[MAGYAR.index(szo[i])]

    output = "".join(output)
    return output
#kodol_dekodol("alma", False)

try:
    szoInput = input("[>] Add meg a szöveget: ")
    print("Mit csináljak?\n  [1] kódol\n  [2] dekódol")
    kodoleInput = int(input("[>] "))
    if kodoleInput not in (1,2):
        raise()
    kodoleInput -= 1
    kodoleInput = bool(kodoleInput)
    print(f"\nKimenet: \"{kodol_dekodol(szoInput, kodoleInput)}\"")
except:
    print("Érvénytelen bemenet.")
    quit()