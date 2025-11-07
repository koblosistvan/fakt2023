dns_hossza, mérések_száma = [int(a) for a in input().split()]
dns = ['?'] * dns_hossza
hiba = False

for i in range(mérések_száma):
    kezdő_pozíció, kód = input().split()
    kezdő_pozíció = int(kezdő_pozíció)
    for i in range(len(kód)):
        pozíció = kezdő_pozíció + i
        if pozíció <= dns_hossza and dns[pozíció-1] in ('?', kód[i]):
            dns[pozíció-1] = kód[i]
        else:
            hiba = True

if hiba:
    print('Hiba!')
else:
    print(''.join(dns))


'''
teszt 1
8 3
1 CAGT
3 GTA
5 ACCT

teszt 2
8 2
2 TTT
7 GG

teszt 3
8 2
2 TTTT
5 GG

'''