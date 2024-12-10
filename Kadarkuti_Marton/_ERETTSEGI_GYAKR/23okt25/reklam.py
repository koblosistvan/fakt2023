feladat_ctr:int = 0
def feladat(leiras:str = "")->None:
    global feladat_ctr
    feladat_ctr += 1
    print('-'*30)
    print(f"{feladat_ctr}. feladat: \n{leiras}")

class Rendel:
    INSTANCES:int = 0
    def __init__(self, data)->None:
        self.nap = int(data[0])
        self.varos = data[1]
        self.darab = int(data[2])

        Rendel.INSTANCES += 1
    
    def __str__(self)->str:
        return f"{self.nap} {self.varos} {self.darab}"
rendelesek:list[Rendel] = []
temp = ""

# 1.
rendelesek = [Rendel(sor.strip().split(' ')) for sor in open("Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\23okt25\\Forras\\3_Reklam\\rendel.txt",'r',encoding="utf-8")]
feladat("rendel.txt beolvasva.")

#2.
feladat()
print("A rendelések száma:",sum(i.darab for i in rendelesek))

#3.
feladat()
prompt:int = 9#int(input("Kérem, adjon meg egy napot: "))
print("A rendelések száma ezen a napon: ",sum(i.darab for i in rendelesek if i.nap == prompt))

#4.
feladat()
nem_volt_rendeles = 0
for rendel in rendelesek:
    if rendel.varos == "NR" and not rendel.darab:
        temp += 1
if nem_volt_rendeles:
    print(nem_volt_rendeles,"nap nem volt a reklámban nem érintett városból rendelés ")
else:
    print("Minden nap volt rendelés a reklámban nem érintett városból")

#5.
feladat()
temp = 0
# megtalalja a maximumot
for rendel in rendelesek:
    if rendel.darab > temp:
        temp = rendel.darab

# megtalalja a maximum helyet (elso alkalom a listaban)
for i in range(Rendel.INSTANCES):
    if rendelesek[i].darab == temp:
        temp = rendelesek[i]
        break
print(f"A legnagyobb darabszám: {temp.darab}, a rendelés napja: {temp.nap}")

#6.
feladat("'osszes' függvénydefiníció")
def osszes(varos:str, nap:int):
    return sum(i.darab for i in rendelesek if i.nap == nap and i.varos == varos)

#7.
feladat()
temp = [0,0,0] # PL, TV, NR
for rendel in rendelesek:
    if rendel.nap == 21:
        match rendel.varos:
            case "PL":
                temp[0] += 1
            case "TV":
                temp[1] += 1
            case "NR":
                temp[2] += 1

print(f"A rendelt termékek darabszáma a 21. napon PL: {temp[0]} TV: {temp[1]} NR: {temp[2]} ")

#8.
feladat()
matrix:list[list[int]] = [] # minta szerinti 3x3 tablazat
temp = [] # benne lesz minden varosnak a rendelesei 0..10, 11..20, 21..30 naponkent szetvalasztva
for varos in ["PL","TV","NR"]:
    temp.append( sum(i.darab for i in rendelesek if i.varos==varos and i.nap <= 10) )  #0..10
    temp.append( sum(i.darab for i in rendelesek if i.varos==varos and 10 < i.nap < 21) ) #11..20
    temp.append( sum(i.darab for i in rendelesek if i.varos==varos and i.nap >= 21) )   #21..30
    matrix.append(temp)
    temp = []

kampany_txt = open("Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\23okt25\\Forras\\3_Reklam\\kampany.txt",'w',encoding="utf-8")
temp = [
    "Napok\t1..10\t11..20\t21..30",
    f"PL\t{matrix[0][0]}\t{matrix[0][1]}\t{matrix[0][2]}",
    f"TV\t{matrix[1][0]}\t{matrix[1][1]}\t{matrix[1][2]}",
    f"NR\t{matrix[2][0]}\t{matrix[2][1]}\t{matrix[2][2]}"
]

for sor in temp:
    print(sor)
    kampany_txt.write(sor)
    kampany_txt.write('\n')
kampany_txt.close()
