with open("esos.txt","r",encoding="utf-8") as f:
    f.readline()
    eso = f.readline().strip().split(" ")
    eso = list(map(int,eso))
print(eso)

feladatCounter = 1
def feladat():
    print("")
    print("𒈙" * 5)
    global feladatCounter
    print(f" < {feladatCounter}.>")
    feladatCounter += 1

# 1.
feladat()

print(f"{sum( [bool(i) for i in eso] )} napon esett az eső.")

# 2.
feladat()
csapadekmentes_idoszakok = "".join([("1" if bool(i) else "0") for i in eso]).split("1")
csapadekmentes_idoszakok = [(len(i) if len(i)>0 else 0) for i in csapadekmentes_idoszakok]
print(f"A leghosszabb csapadékmentes időszak {max(csapadekmentes_idoszakok)} napig tartott.")

# 3.
feladat()

ket_napi_max = 0
for i in range(len(eso)-1):
    temp = eso[i]+eso[i+1]
    if temp > ket_napi_max:
        ket_napi_max = temp
print(f"A legtöbb csapadék két nap között {ket_napi_max} mm.")

# 4.
feladat()

