futás = True
motorjár = False
sebesség = 0
while futás:
    parancs = input("> ")
    if parancs == "indít":
        if motorjár:
            print("A motor már jár.")
        else:
            print("A motor elindult.")
            motorjár = True
    if parancs == "leáll":
        if motorjár:
            print("A motor leállt.")
        else:
            print("A motor már le van állítva.")
    if parancs == "gyorsít":
        if motorjár == False:
            print("A motor áll.")
        else:
            gyorstás = int(input("Gyorsítás: "))
            sebesség = sebesség + gyorsítás
            print(sebesség)
    if parancs == "lassít":
        if motorjár == False:
            print("A motor áll.")
        elif sebesség <= 0:
            print("A sebesség 0.")
        else:
            lassítás = int(input("Lassítás: "))
            sebesség = sebesség - lassítás
            if sebesség < 0:
                sebesség = sebesség * 2
    if parancs == "elég":
        futás = false
        print("Viszlát!")
