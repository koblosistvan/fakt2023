álllapot = False
Futás = True
sebesség = 0

while True:
    parancs = input("> ")
    if parancs == "indít":
        if álllapot:
            print("A motor már megy")
        else:
            print(" A MOTOR ELINDÚLT")
            álllapot = True
    elif parancs == "leáll":
        if álllapot and sebesség == 0:
            álllapot = False
            print("A motor leállt.")
        else:
            print("A motor nem megy")
    elif parancs == "gyorsít":
        sebesség += 1
    elif parancs == "lassít":
        sebesség -= 1
    elif parancs == "elég":
        Futás = False
        print("Cső")
    else:
        print("Nem értem a parancsot, próbáld újra! ")










