def bumm(ettol,eddig,tiltott):
    output = [i for i in range(ettol, eddig+1)]
    tiltott = str(tiltott)
    for i in range(len(output)):
        if str(output[i]).count(tiltott) != 0 or output[i]%int(tiltott) == 0:
            output[i] = "!!"
        output[i] = str(output[i])
    print(", ".join(output))

bevitel = []
sys = ["kezdőszámát", "utolsó számát", "tiltott számát"]
for i in range(3):
    try:
        bevitel.append(int(input(f"[>] Add meg a sorozat {sys[i]}: ")))
        if not (bevitel[i] == int(bevitel[i])):
            raise()
        if bevitel[i] <= 0:
            raise()
    except:
        print("Érvénytelen bemenet.")
        quit()

bumm(bevitel[0],bevitel[1],bevitel[2])