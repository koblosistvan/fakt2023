forrás = open("lottosz.dat", mode="r", encoding="utf-8")


számok = []

for sor in forrás:
    adat = sor.strip().split(" ")
    adat_int = [int(a) for a in adat]
    számok.append(adat_int)

forrás.close()

utolso_heti = input("Add meg az 52. heti lottószámokat. ")

ötvenkettedik = utolso_heti.split(" ")

hetek = []
for i in ötvenkettedik:
    hetek.append(i)

rendezett = sorted(hetek)

számok.append(rendezett)
print(rendezett)

bekért_szám = int(input("1 és 52 közt adj meg egy egész számot"))
print(számok[bekért_szám-1])








