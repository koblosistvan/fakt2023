képletek_száma, sorok_száma = [int(s) for s in input().split()]
képletek = []
for i in range(képletek_száma):
    képlet = [int(s) for s in input().split()] 
    képletek.append([képlet[0], képlet[1], képlet[1]/képlet[0], i+1])
    # sor, érték, egy sorra jutó érték, sorszám

képletek.sort(key=lambda a: a[2], reverse=True)
puska = []
maradek_hely = sorok_száma
fontosság = 0
for i in range(len(képletek)):
    if képletek[i][0] <= maradek_hely:
        maradek_hely -= képletek[i][0]
        fontosság += képletek[i][1]
        puska.append(képletek[i][3])

print(len(puska), fontosság)
print(*puska, sep=' ')


'''
teszt 1
4 1
1 2
1 5
1 3
1 7

teszt 2
4 7
5 2
4 2
2 2
1 2

teszt 3
6 10
2 3
1 4
7 10
3 5
4 2
8 12

'''