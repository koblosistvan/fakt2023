def szamol_pi(k):
    pi_nelkul = 0
    for i in range(k):
        if i % 2 == 0:
            pi_nelkul += 1 / (2 * i + 1)
        else:
            pi_nelkul -= 1 / (2 * i + 1)

    pi = 4 * pi_nelkul
    return pi


n = int(input("Add meg, hány tagot szeretnél felhasználni a közelítéshez: "))
approx_pi = szamol_pi(n)
print(f"π közelítő értéke {n} tag felhasználásával: {approx_pi}")
