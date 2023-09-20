import random

mettol = 0
meddig = 1000
a = random.randint(mettol + 1, meddig + 1)
print(f'A szám: {mettol} - {meddig} intervallumban van.')

probak = 0
while probak < meddig+1:
    tipp = int(input('Tippelj egy számot: '))
    if tipp == a:
        print('Forró, eltaláltad a számot!')
        print(f'{probak + 1} tippből találtad ki.')
        break
    elif tipp < a:
        if a - tipp <= 20:
            print('Meleg, nagyobb a szám a tippednél, de közel jársz a megoldáshoz.')
        elif a - tipp <= 40:
            print('Langyos, nagyobb a szám a tippednél, de nem jársz messze a megoldástól.')
        else:
            print('Hideg, nagyobb a szám a tippednél és nem jársz közel a megoldáshoz.')
    else:
        if tipp - a <= 20:
            print('Meleg, kisebb a szám a tippednél, de közel jársz a megoldáshoz.')
        elif tipp-a <= 40:
            print('Langyos, kisebb a szám a tippednél, de nem jársz messze a megoldástól.')
        else:
            print('Hideg, kisebb a szám a tippednél és nem jársz közel a megoldáshoz.')
    probak += 1
    if probak == meddig-5:
        print("Már csak 5 próbás van hátra")
if probak == meddig:
    print('Béna vagy.')
