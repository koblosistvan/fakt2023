'''
def kinyert(pakli, húzás):
    # kiszámoljuk a pontokat
    pont_a = 0
    pont_b = 0
    for i in range(len(pakli)):
        if húzás[i] == 'A':
            pont_a += pakli[i]
        elif húzás[i] == 'B':
            pont_b += pakli[i]

    # eredmény meghatározása
    if pont_a > 21 and pont_b > 21:
        return 'A és B befuccsolt, döntetlen'
    elif pont_a > 21:
        return 'A befuccsolt, B nyert'
    elif pont_b > 21:
        return 'A nyert, B befuccsolt'
    elif pont_a == pont_b:
        return 'döntetlen'
    elif pont_a > pont_b:
        return 'A nyert'
    else:
        return 'B nyert'


print(kinyert([2, 3, 7, 2, 10, 3, 4], 'AABBABB'))
print(kinyert([2, 3, 7, 2, 10, 3, 4], 'ABBAABB'))
print(kinyert([2, 3, 7, 2, 10, 3, 4], 'ABABABB'))
'''

ékezetes_betűk = 'öüóőúéáűíÖÜÓŐÚÉÁŰÍ'
def ékezetes(szó):
    for k in szó:
        if k in ékezetes_betűk:
            return True
            break
    else:
        return False

def szűr(mondat):
    szavak = mondat.split(' ')
    for i in range(len(szavak)):
        
