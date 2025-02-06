#1
print("1. feladat")
forrasinput = input("Adja meg a bemeneti fájl nevét!")
sorinput = int(input("Adja meg egy sor számát!"))
oszlopinput = int(input("Adja meg egy oszlop számát!"))
resztabla = [[[1,2,3],[1,2,3]], [[1,2,3],[4,5,6]], [[1,2,3],[7,8,9]], [[4,5,6],[1,2,3]], [[4,5,6],[4,5,6]], [[4,5,6],[7,8,9]], [[7,8,9],[1,2,3]], [[7,8,9],[4,5,6]], [[7,8,9],[7,8,9]]]#sor,oszlop

#2
forras = open(f"PigaiPéter\\érettségi\\2021oktinfo\\4_Sudoku\\{forrasinput}", mode="r", encoding="utf-8")
sorok = []
lepes = []
for sor in forras:
    adat = sor.strip().split(" ")
    if len(adat) == 3:
        break
    sorok.append(adat)
for sor in forras:
    adat = sor.strip().split(" ")
    lepes.append(adat)
forras.close()

#3
print("3. feladat ")
if sorok[sorinput][oszlopinput] == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {sorok[sorinput][oszlopinput]}")
for i in range(len(resztabla)):
    if sorinput in resztabla[i][0] and oszlopinput in resztabla[i][1]:
        print(f"A hely a(z) {i+1} résztáblázathoz tartozik.")
    
#4
print("4. feladat")
ossz = 0
kitoltetlen = 0
for i in range(len(sorok)):
    kitoltetlen += sorok[i].count("0")
    ossz += len(sorok[i])
print(f"Az üres helyek aránya: {round(kitoltetlen/ossz * 100, 1)}%")

#5
for i in range(len(lepes)):
    print(f"A kiválasztott sor: {lepes[1]} oszlop: {lepes[2]} a szám: {lepes[0]}")
    if sorok[lepes[1]][lepes[2]] != 0:
        print("A helyet már kitöltötték")
    else:
        for j in range(len(resztabla)):
            if lepes[1] in resztabla[j][0] and lepes[2] in resztabla[j][1]:
                for k in range(len(resztabla[j][0])):
                    for l in range(len(resztabla[j][0])):
                        if lepes[0] == sorok[resztabla[j][k]][resztabla[j][l]]:
                            print("Az adott résztáblázatban már szerepel a szám")
                            break
                        break
                    break
            else:
                if lepes[0] in sorok[lepes[1]]:
                    print("Az adott sorban már szerepel a szám")
                else:
                    for o in range(len(sorok)):
                        if lepes[0] == sorok[o][lepes[2]]:
                            print("Az adott oszlopban már szerepel a szám")
                        else:
                            print("A lépés megtehető")
            
