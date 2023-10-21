l1 = [80, 81, 65, 50, 19, 45, 37, 14, 95, 48, 69, 54, 77, 72, 64, 27, 22]
l2 = [53, 99, 15, 74, 84, 71, 80, 85, 36, 71, 61, 2, 60, 10, 62, 42, 25]

# összefűzés
print(l1+l2)

# összeg meghatározása
összeg = [l1[i] + l2[i] for i in range(len(l1))]
print(összeg)

# különbség meghatározása
különbség = [l1[i] + l2[i] for i in range(len(l1))] # írd át
print(különbség)

# növekmény meghatározása
növekmény = [l1[i+1] - l1[i] for i in range(len(l1)-1)] # írd át
print(max(növekmény))

# index meghatározása
hatos_id = l1.index(45)
print(hatos_id)
legnagyobb_id = l1.index(max(l1))
print(legnagyobb_id)

# legnagyobb különbség
legnagyobb_különbség = [l1[i] - l1[k] for i in range(len(l1)) for k in range(len(l1))] # írd át
legnagyobb_különbség_id = max(legnagyobb_különbség) # írd át

# növekmény
növekmény_érték = [l1[i+1]-l1[i] for i in range(len(l1)-1)]
print(növekmény_érték)
növekmény_arány = [] # írd át

# legnagyobb növekmény index
legnagyobb_növekmény = 0 # írd át
legnagyobb_növekmény_id = 0 # írd át

# szűrés
ötven_fölött = [a for a in l1 if a > 50]
print(ötven_fölött)

# szűrt összesítés
ötven_fölötti_összeg = sum(ötven_fölött)
ötven_fölötti_átlag = sum(ötven_fölött) / len(ötven_fölött)
ötven_alatti_összeg = sum([a for a in l1 if a < 50])

párosok_összege = sum([a for a in l1 if a % 2 ==0]) # írd át
harmincasok_átlaga = sum([a for a in l1 if 30 <= 0 < 40]) # írd át

# szűrt min/max
legnagyobb_harminc_alatti = max([a for a in l1 if a < 30])

legnagyobb_páros = max([a for a in l1 if a % 2 == 0]) # írd át
