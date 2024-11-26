# 1. feladat
forrás = open('dobozok.txt', mode='r', encoding='utf-8')

forrás.readline()
dobozok = []
for sor in forrás:
    dobozok.append([int(a) for a in sor.strip().split(' ')])
forrás.close()

# 2. feladat
darabszámok = [doboz[0] for doboz in dobozok]
doboz_átlag = sum(darabszámok)/len(darabszámok)
if doboz_átlag == sum(darabszámok)//len(darabszámok):
    print('A játékokat egyenletesen el lehet osztani a dobozokban.')
    print(f'Játékok dobozonkénti átlagos száma: {sum(darabszámok)//len(darabszámok)}')
else:
    print('A játékokat nem lehet egyenletesen elosztani a dobozokban.')
    print(f'Játékok dobozonkénti átlagos száma: {doboz_átlag:.2f}')

# 3. feladat
max_darab = max(darabszámok)
legnagyobbak = [str(i+1) for i in range(len(darabszámok)) if darabszámok[i] == max_darab]
print(f"Legtöbb játék egy dobozban ({max_darab} db) a következő dobozokban volt: {' '.join(legnagyobbak)}")

# 4. feladat
játék_stat = {}
for doboz in dobozok:
    for játék in doboz[1:]:
        if játék in játék_stat:
            játék_stat[játék] += 1
        else:
            játék_stat[játék] = 1

max_játék = 0
for játék, darab in játék_stat.items():
    if darab > max_játék:
        max_játék = darab
print("Legnépszerűbb játék(ok):", end=" ")
for játék, darab in játék_stat.items():
    if darab == max_játék:
        print(játék, end="")
print()

# 5. feladat
print("Melyik dobozokból kell elvenni:")
for i in range(len(dobozok)):
    if dobozok[i][0] > doboz_átlag:
        print(f"{i+1}. dobozból {int(dobozok[i][0] - doboz_átlag)} db játékot")

# 6. feladat
játék_kódok = set([játék for játék, darab in játék_stat.items()])
print("A hiányos dobozokba melyik játék rakható:")
for i in range(len(dobozok)):
    if dobozok[i][0] < doboz_átlag:
        nincs_benne = [str(kód) for kód in játék_kódok if kód not in dobozok[i][1:]]
        print(f"{i+1}. doboz: {' '.join(nincs_benne)}")
