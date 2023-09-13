álllapot = False
Futás = True


while True:
    parancs = input("> ")
    if parancs == "indít":
        if álllapot:
            print("A motor már megy")
        else:
            print(" A MOTOR ELINDÚLT")
            álllapot = True
    elif parancs == "leáll":
        print("A motor leállt.")
        álllapot = "áll"
    elif parancs == "elég":
        Futás = False
    else:
        print("Nem értem a parancsot, próbáld újra! ")










