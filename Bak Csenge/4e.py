szöveg = input("Egy szöveg: ")
magánhangzók = "öüóeuoiőúaéáűí"
magánhangzók_száma = 0
magánhangzók_szövegbe = ""
for i in range(len(szöveg)):
    if szöveg[i].lower() in (magánhangzók):
        magánhangzók_szövegbe += szöveg[i]

        magánhangzók_száma += 1
print(magánhangzók_szövegbe)
print(magánhangzók_száma)

gy_szám =0
for i in range(len(szöveg)-1):
    if szöveg[i].lower() == "g" and szöveg[i+1].lower() == "y":
        gy_szám += 1

print(gy_szám)







