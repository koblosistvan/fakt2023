feladatCounter = 0
def feladat():
    global feladatCounter
    feladatCounter += 1
    print("\n" + "-" * 30 + f"\n{feladatCounter}. feladat:\n")


# bemenet
K = 71

def collatz(n): # n = 27
    r = [n]
    while n != 1:
        if n%2 == 0:
            n = n// 2
        else:
            n = 3*n +1
        r.append(n)
    return r

# 1.
feladat()
sorozat = collatz(K)
print( "; ".join(map(str, sorozat)))

# 2.
feladat()
kettesFeladatSubstring = False
for i in range(len(sorozat)):
    if sorozat[i] > K:
        kettesFeladatSubstring = True
        break

kettesFeladatSubstring = "Van" if kettesFeladatSubstring else "Nincsen"
print(f"{kettesFeladatSubstring} olyan eleme {K} sorozatának, amely nagyobb, mint {K}.")

# 3.
feladat()
def vanNagyobb(n):
    c = collatz(n)
    for i in range(len(c)):
        if n < c[i]:
            return True
    return False

data = [collatz(i) for i in range(1, K + 1)]

for i in range(1,K+1):
    print("")
    temp = "Van" if vanNagyobb(i) else "Nincsen"
    print(f"{i} : {temp}")
    print( "; ".join(map(str, data[i - 1])))

# 4.
feladat()
negyesFeladat = []

def nagyobbMintK(n):
    if n > K:
        return True
    return False

for i in range(len(data)):
    temp = [nagyobbMintK(h) for h in data[i]]
    #print(temp,temp.count(False))
    if temp.count(True) == 0:
        negyesFeladat.append(len(data[i]))
print(f"A leghosszabb olyan sorozat, amelynek ≤{K} minden eleme {max(negyesFeladat)} elemből áll.")
