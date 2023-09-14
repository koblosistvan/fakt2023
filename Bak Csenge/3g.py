import random

random = random.randint(0,2)
k_p_o = ["kő", "papír", "oló"]

én = 0
gép = 0

kő = ["olló", "kő"]
papír = ["papír", "kő"]
olló = ["papír", "olló"]

lista = []


while én < 3 or gép < 3:
    input_e = input(" ")
    print(k_p_o[random])
    lista.append(input_e, k_p_o[random])
    if lista == kő:










