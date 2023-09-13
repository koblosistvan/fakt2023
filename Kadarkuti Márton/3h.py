futás = True
motor_jár = False
speed = 0

while futás:
    parancs = input("> ")
    if speed != 0:
        print(f"Sebesség: {speed}km/h")

    if parancs == "indul":                  #INDUL
        if motor_jár:
            print("A motor már jár.")
        else:
            print("A motor elindult.")
            motor_jár = True
            print("Sebesség: 1km/h")
            speed = 1

    elif parancs == "leáll":
        speed = 0                       #LEÁLL
        if not motor_jár:
            print("A motor le van állítva.")
        else:
            print("A motor leállt.")
            motor_jár = False


    elif parancs == "gyorsít":                  #GYORSÍT
        if not motor_jár:
            print("Nem lehet gyorsítani,")
            print("a motor jelenleg le van állítva.")
        else:
            speed += 1
            print(f"A sebesség növekedett. ({speed}km/h)")

    elif parancs == "lassít":                   #LASSÍT
        if not motor_jár:
            print("Nem lehet lassítani,")
            print("a motor jelenleg le van állítva.")
        else:
            if speed > 0:
                speed -= 1
                print(f"A sebesség csökkent. ({speed}km/h)")
            else:
                motor_jár = False
                print("A motor elérte a 0km/h sebességet,")
                print("A motor leállt.")

    elif parancs == "elég":                     #ELÉG
        print("Viszlát!")
        speed = 0
        futás = False
    elif parancs == "":
        print("")
    else:
        print("Nem értem.")