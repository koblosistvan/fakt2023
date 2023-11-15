import random



kor_x = 0
kor_y = 0
kor_sugar = 5

pontok_szama = 1000

koron_beluli_pontok = 0


for i in range(pontok_szama):
    x = random.uniform(-kor_sugar, kor_sugar)
    y = random.uniform(-kor_sugar, kor_sugar)

    tavolsag_kozepponttol = (x - kor_x) ** 2 + (y - kor_y) ** 2
    if tavolsag_kozepponttol <= kor_sugar ** 2:
        koron_beluli_pontok += 1


print("A koron beluli pontok szama:", koron_beluli_pontok)
