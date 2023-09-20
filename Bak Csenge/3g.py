import random

k_p_o = ["kő", "papír", "olló"]   # todo: listák használata, változó nevek beszédesek

én = 0
gép = 0
én_k = 0
gép_k = 0

kő = ["olló", "kő"]     # todo: győztes kombók megadása
papír = ["papír", "kő"]
olló = ["papír", "olló"]
számolás = 0
káromkodás = 0

print('Ha ki szeretnél lépni, akkor írd be a "k" betűt!\n')
while én < 3 and gép < 3:
    létezik = True
    izé = random.randint(0, 2)
    input_e = input("")
    if input_e != "kő" and input_e != "papír" and input_e != "olló" and input_e != "k" and input_e.find("basszus"):
        print("A beírt szöveg nem értelmezhető, kérlek próbáld újra!\n")
        létezik = False
        számolás += 1
        if számolás == 3:
            print("Hallod?! Hányszor fogod még elrontani?! Számolom ám!")
    if input_e.find("basszus") != -1:
        print("Ne káromkodj, ezért büntit kapsz >:C")
        én -= 1
        káromkodás += 1
        print(f"Állás: {én = }\t\t{gép = } \n")
        létezik = False
    if input_e == "k":
        if input("Biztos ki szeretnél lépni?(Jap - igen, Nop - nem) ") == "Jap":
            print("Bénaaaa, feladtad")
            én = 0
            gép = 3
            break
        else:
            print("\nFigyelj már oda mit írsz!! >:c ")
            print(f"Na jóvan, ha annyira szeretnéd folytatni, folytasd.... Az aktuális állás a következő: {én=} {gép=}")
    if létezik:
        print(k_p_o[izé])
    if [input_e, k_p_o[izé]] == kő or [k_p_o[izé], input_e] == kő:
        if input_e == "kő":
            én += 1
        else:
            gép += 1
    elif [input_e, k_p_o[izé]] == papír or [k_p_o[izé], input_e] == papír:
        if input_e == "papír":
            én += 1
        else:
            gép += 1
    elif [input_e, k_p_o[izé]] == olló or [k_p_o[izé], input_e] == olló:
        if input_e == "olló":
            én += 1
        else:
            gép += 1
    if létezik:
        print(f"Állás: {én=} {gép=} \n")
    if (én == 3 or gép == 3) and input("Szeretnél még egyet? (Jap - igen) ") == "Jap":
        if én > gép:
            print("Én győztem! Hehee :DD")
            én_k += 1
        else:
            print("A gép győzött :'C")
            gép_k += 1

        print(f"Körönkénti győzelmek: {én_k=} {gép_k=}")
        print(f"Félregépelések száma: {számolás}")
        print(f"Káromkodások száma: {káromkodás}")
        print("Jöhet a kövi kör:")
        én = 0
        gép = 0
    elif létezik and (én == 3 or gép == 3):
        if én > gép:
            print("Én győztem! Hehee :DD")
            én_k += 1
        else:
            print("A gép győzött :'C")
            gép_k += 1

        print(f"Körönkénti győzelmek: {én_k=} {gép_k=}")
        print(f"Félregépelések száma: {számolás}")
        print(f"Káromkodások száma: {káromkodás}")









