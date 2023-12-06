x = int(input("Első kiírandó szám: "))
y = int(input("Utolsó kiírandó szám: "))
z = int(input("Hányasával legyenek kiírva: "))
for i in range(x, y + 1, z):
    print(i)
