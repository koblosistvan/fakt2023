def kinyert(pakli, huzasok):
    A_sum = 0
    B_sum = 0
    eredmeny = ["A nyert.", "B nyert.", "Döntetlen."]
    for i in range(len(huzasok)):
        if huzasok[i] == "A":
            A_sum += pakli[i]
        if huzasok[i] == "B":
            B_sum += pakli[i]
    if A_sum > B_sum:
        eredmeny = eredmeny[0]
    elif B_sum > A_sum:
        eredmeny = eredmeny[1]
    else:
        eredmeny = eredmeny[2]
    return eredmeny

#PELDA = [ [2,3,7,2,10,3,4] ,["A", "A", "B", "B", "A", "B"] ]
#print(kinyert(PELDA[0], PELDA[1]))




try:
    pakliInputString = input("[>] Add meg a pakli kártyáit vesszővel elválasztva: ")
    pakliInput = pakliInputString.strip().split(",")
    for i in range(len(pakliInput)):
        pakliInput[i] = int(pakliInput[i])
    huzasokInput = input(
        "[>] Add meg a húzások sorrendjét vesszővel elválasztva:\n  Példa: A,A,B,A,B                  [>] ")
    huzasokInput = huzasokInput.strip().split(",")
    if len(pakliInput) < len(huzasokInput):
        raise()
    eredmeny = kinyert(pakliInput, huzasokInput)
except:
    print("Érvénytelen bemenet.")

print("-"*30)
print(f"A játék eredménye: {eredmeny}")
print(f"Pakli: {pakliInputString.replace(',',', ')}")
print(f"Húzási sorrend: {', '.join(huzasokInput)}")
