with open("esos.txt","r",encoding="utf-8") as f:
    f.readline()
    eso = f.readline().strip().split(" ")
    eso = list(map(int,eso))
print(eso)

feladatCounter = 1
def feladat():
    global feladatCounter
    print(f"\n{feladatCounter}.")
    feladatCounter += 1

# 1.
feladat()

print(f"{sum( [bool(i) for i in eso] )} napon esett az eső.")

# 2.
feladat()
csapadekmentes_idoszakok = str(list(map(str,eso))).split()