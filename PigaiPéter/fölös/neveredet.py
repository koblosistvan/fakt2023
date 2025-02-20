def NevKivalaszt(nevlista, kezdőbetű, maxhossz, nem, eredete):
    lista = []
    for név in nevlista:
        adottnév = []
        név_lista = név.strip().split(",")
        if (név_lista[0][0] == kezdőbetű) and (len(név[0]) == maxhossz) and (eredete not in név_lista[1]):
                adottnév.append(név_lista[0])
                adottnév.append(nem)
        lista.append(', '.join(adottnév))
    return lista
                

