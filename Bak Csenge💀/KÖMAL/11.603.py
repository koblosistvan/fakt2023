a_bekért = (input("Adj meg egy számot! "))
b_bekért = (input("Adj meg egy számot! "))

eredmény = 0
futtatás = len(a_bekért) if len(a_bekért) > len(b_bekért) else len(b_bekért)


for i in range(futtatás):
    if i > len(a_bekért)-1:
        a_szám_i = a_bekért[len(a_bekért) - 1]
    else: a_szám_i = a_bekért[i]

    if i > len(b_bekért)-1:
        b_szám_i = b_bekért[len(b_bekért) - 1]
    else: b_szám_i = b_bekért[i]


    if int(a_szám_i) % int(b_szám_i) == 0:
        eredmény += 1
    if int(b_szám_i) % int(a_szám_i) == 0:
        eredmény += 1


    for j in range(i, futtatás):
        if j > len(a_bekért)-1:
            a_szám_j = a_bekért[len(a_bekért)-1]
        else: a_szám_j = a_bekért[j]
        if j > len(b_bekért)-1:
            b_szám_j = b_bekért[len(b_bekért)-1]
        else: b_szám_j = b_bekért[j]


        if int(a_szám_i) % int(b_szám_j) == 0:
            eredmény += 1
        if int(b_szám_j) % int(a_szám_i) == 0:
            eredmény += 1


print(eredmény)










