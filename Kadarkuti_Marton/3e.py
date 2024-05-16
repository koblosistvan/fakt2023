# 1/1 - 1/3 + 1/5 - 1/7 + 1/9 ...

print("-A program közelíti a pí értékét a Leibniz képlettel-")

print("**Referencia: A sorozat 10000-es precizitásnál 4 számjegyre konvergál.")
r = int(input(">Precizitás: "))*2

p = 0
j = 1      #iteráció száma

for i in range(1, r, 2):
    if not j % 2:
        i = (-1)*i
    j += 1
    p = p + 4/i
    print(f"[{j-1}.] {p}")
    print("------------------")


p = str(p)

PI = ["3", ".", "1", "4", "1", "5", "9", "2", "6", "5", "3", "5", "8", "9", "7"]

j = 0

for k in range(15):
    if p[k] == PI[k]:
        j += 1
        continue
    else:
        break

if j <= 1:
    j = 2

print(f"\n<<< A végeredmény {j-2} tizedesjegyre pontos. >>>")
