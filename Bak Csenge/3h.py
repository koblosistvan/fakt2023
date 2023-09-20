import random

veletlen = random.randint(0, 1000)
tipp = -1

while veletlen != tipp:
    tipp = int(input("A tippelt szám: "))
    if tipp < veletlen:
        print("A tipped kisebb")
    elif tipp > veletlen:
        print("A tipped nagyobb")
    else:
        print("Talált")
    if abs(veletlen - tipp) <= 5 and abs(veletlen - tipp) != 0:
        print("Meleg\n")
    elif abs(veletlen - tipp) <= 10 and abs(veletlen - tipp) != 0:
        print("Langyos\n")
    elif abs(veletlen - tipp) > 10:
        print("Hideg\n")




