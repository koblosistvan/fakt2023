pontok = open("pontok.txt", mode="r", encoding="utf-8")

x_pont = []
y_pont = []

for i in pontok:
    t = i.split(" ")
    x_pont.append(float(t[0]))
    y_pont.append(float(t[1]))

if len(x_pont) == len(y_pont):
    print("y")


x_kor = float(input("Add meg a kör középpontjának [x] koordinátáját: "))
y_kor = float(input("Add meg a kör középpontjának [y] koordinátáját: "))
r = float(input("Add meg a kör [sugarát]: "))
r = r*r

pontokszama = [0, 0, 0]    #belül, rajta, kívül
for i in range(len(x_pont)):
    d = (x_kor - x_pont[i])**2 + (y_kor - y_pont[i])**2
    if d < r:
        pontokszama[0] += 1
    elif d == r:
        pontokszama[1] += 1
    else:
        pontokszama[2] += 1


print(f"\n{pontokszama[0]} pont van a [[körvonalon belül]].")
print(f"{pontokszama[2]} pont van a [[körvonalon kívül]].")
print(f"{pontokszama[1]} pont van a [[körvonalon]].")
print("-"*10)
