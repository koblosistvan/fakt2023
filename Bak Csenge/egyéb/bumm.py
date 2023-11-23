
ettől = int(input("Ettől: "))
eddig = int(input("Eddig: "))
tiltott = int(input("A tiltott szám: "))
szám_tömb = []

for i in range(ettől, eddig+1):
    szám_tömb.append(int(i))


for i in range(len(szám_tömb)):
    if szám_tömb[i] % tiltott != 0 and str(tiltott) not in str(szám_tömb[i]):
        print(szám_tömb[i], end=" ")
    else:
        print("!!", end=" ")








