

kartyak = [2, 10, 5, 3, 10]

jatekosok = 'AABBABB'

def kinyert(pakli,huzas):
    #pontszamolas
    pont_a=0
    pont_b=0
    for i in range(len(pakli)):
        if huzas[i] == 'A':
            pont_a += pakli[i]

        elif huzas[i] == 'B':
            pont_b += pakli[i]

    #van fuccs
    if pont_a > 21 and pont_b > 21:
        return 'mindeki befuccsolt döntetlen'

    elif pont_a > 21 :
        return 'A fuccsolt B nyert'

    elif pont_b > 21:
        return 'B befuccsolt A nyert'

    elif pont_b == pont_a:
        return 'döntetlen'

    elif pont_a > pont_b:
        return 'A nyert'

    else:
        return 'B nyert'

print(kinyert([2, 10, 5, 3, 10, 4, 1],'AABBAAB'))
print(kinyert([2, 10, 5, 3, 10, 3, 1],'ABBABAB'))
print(kinyert([2, 10, 5, 3, 10, 1, 6],'AABBAAB'))

