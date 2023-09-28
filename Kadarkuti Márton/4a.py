import random
l = []
páros = 0
páratlan = 0
hatosok_száma = 0
prímek_száma = 0
PRÍMEK = (2, 3, 5)
számláló = [0, 0, 0, 0, 0, 0]
string = ""

for i in range(100):
    i = random.randint(1, 6)
    l.append(i)

    if i % 2 == 0:
        páros += 1
    else:
        páratlan += 1

    if i == 6:
        hatosok_száma += 1

    if i in PRÍMEK:
        prímek_száma += 1

    string = string + str(i)


print(f"A generált számok:\n{l}")
print(string)
print(f"\n{len(l)} elem")
print(f"Hatosok száma: {hatosok_száma}")
print(f"Páros számok száma: {páros}")
print(f"Páratlan számok száma: {páratlan}")
print(f"Prímszámok száma: {prímek_száma}")

egyes_után_kettes = 0
for i in range(len(l)-1):
    if l[i] == 1 and l[i+1] == 2:
        egyes_után_kettes += 1
    else:
        continue

print(f"Ennyiszer fordult elő, hogy 1-es után 2-est dobtunk: {egyes_után_kettes}")

#egymás után három növekvő sorrendben:
andor = 0
for i in range(len(l)-2):
        if l[i] < l[i+1] < l[i+2]:
            andor += 1
        else:
            continue
print(f"Ennyiszer fordult elő, hogy három egymás utáni szám növekvő sorrendben jött létre: {andor}")

