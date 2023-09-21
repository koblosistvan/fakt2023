import random

geppont = 0
jatekospont = 0

for i in range(1, 4):
    jatekos = input(f'({i}. kör) Írd ide: kő, papír, olló\n> ')

    gep = random.randint(1, 4)

    if gep == 1:
        gep = "kő"
    elif gep == 2:
        gep = "papír"
    else:
        gep = "olló"

    if gep == "kő" and jatekos == "olló" or gep == "papír" and jatekos == "kő" or gep == "olló" and jatekos == "papír":
        print('A gép nyert')
        geppont += 1
    elif gep == jatekos:
        print('Döntetlen')
    else:
        print('Te nyertél!')
        jatekospont += 1
    print("A gép választása: " + gep)
    print(f"Állás: {jatekospont}-{geppont}\n")

print("---------------------------")
if geppont > jatekospont:
    print("Sajnos összesítve nem nyertél :(")
elif geppont < jatekospont:
    print("Nyertél :)")
else:
    print("Döntetlen!")
