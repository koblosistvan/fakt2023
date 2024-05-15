import random
A = 1
B = 100
n = random.randint(A, B)
elso = True

print(f"\n-A program gondolt egy számra {A} és {B} között-")

x = B+1
m = 1

while x != n:
    if not elso:
        x = int(input("\nPróbáld újra: "))
    else:
        x = int(input("\nTippelj: "))
        elso = False

    if x == n:
        break

    if x < A or x > B:
        print("<nagyon hideg>")
    elif abs(x-n) > 20:
        print("<hideg>")
    elif 10 <= abs(x-n) <= 20:
        print("<langyos>")
    elif abs(x-n) < 10:
        print("<meleg>")
    m += 1

print("")

if m < 10:
    print("Nagyon ügyes!")
else:
    print("Ügyes!")
print(f"(<{m}.> próbálkozás.)")
