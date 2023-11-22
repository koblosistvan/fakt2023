with open("kerekparverseny.txt", "r", encoding="utf-8") as f:
    szakaszok = []
    HOSSZ = f.readline()
    HOSSZ = HOSSZ[2]+HOSSZ[3]
    HOSSZ = int(HOSSZ)
    for sor in f:
        sor = int(sor.strip())
        szakaszok.append(sor)

print(HOSSZ)
print(szakaszok)
l = len(szakaszok)

for i in range(l):
    pass