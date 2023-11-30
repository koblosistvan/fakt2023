EKEZETES_BETUK = "áÁéÉíÍóÓöÖőŐúÚüÜűŰ"
EKEZET = []
for i in range(0, 18):
    EKEZET.append(EKEZETES_BETUK[i])
EKEZET_SET = set(EKEZET)

def ekezetes(szo):
    szo = set(str(szo))
    if len(szo.intersection(EKEZET_SET) != 0):
        return True
    else:
        return False

while True:
    j = input("> ")
    print(ekezetes(j))