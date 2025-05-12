def binomkeres(lista, a, bal, jobb):
    if jobb < bal:
        return -1
    else:
        kozep = (bal+jobb)/2
        if lista[kozep] == a:
            return kozep
        elif a < lista[kozep]:
            return binomkeres(lista, a, bal, kozep-1)
        else:
            return binomkeres(lista, a, kozep+1, jobb)
