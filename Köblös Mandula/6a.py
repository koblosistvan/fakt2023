forrás = open("../../programozás/6a-hallgatok.txt", mode='r', encoding='utf-8')

szül_dátum = []
kezdés = []
befejezés = []


forrás.readline()

for sor in forrás:
    adat = sor.strip().split(" ")
    szül_dátum.append([int(adat[0]), int(adat[1]), int(adat[2])])
    kezdés.append(int(adat[3]))
    befejezés.append(int(adat[4]))

forrás.close()

életkor = int(input("Adj meg egy életkort: "))

fiatalabb = 0
for i in range(len(szül_dátum)):
    if befejezés[i] - szül_dátum[i][0] < életkor:
        fiatalabb += 1
if fiatalabb > 0:
    print("Van olyan hallgató aki ennél fiatalabban szerzett diplomát.")
else: print("Nincs olyan hallgató aki ennél fiatalabban szerzett diplomát.")


for i in range(len(szül_dátum)):
    if befejezés[i] - szül_dátum[i][0] < életkor:
        print("Van olyan hallgató aki ennél fiatalabban szerzett diplomát.")
        break
else:
    print("Nincs olyan hallgató aki ennél fiatalabban szerzett diplomát.")

szülinap = [2007, 4, 12]
for i in range(len(szül_dátum)):
    if szül_dátum[i][1:] == szülinap[1:]:
        print("Van olyan akinek ugyanakkor van a szülinapja.")
        break
else:
    print("Nincs olyan akinek ugyanakkor van a szülinapja.")

ugyanakkor = 0
for i in range(len(szül_dátum)):
    if szül_dátum[i][1:] == szülinap[1:]:
        ugyanakkor += 1
print(f'{ugyanakkor} hallgatónak van ugyanakkor szülinapja.')

legfiatalabb_id = 0
for i in range(len(szül_dátum)):
    if befejezés[i] - szül_dátum[i][0] < befejezés[legfiatalabb_id] - szül_dátum[legfiatalabb_id][0]:
        legfiatalabb_id = i
print(f'A legfiatalabban végzett hallgató ekkor született: {szül_dátum[legfiatalabb_id][0]:0>2d}.{szül_dátum[legfiatalabb_id][1]:0>2d}.{szül_dátum[legfiatalabb_id][2]:0>2d}')

végzett2016 = 0
for i in range(len(szül_dátum)):
    if befejezés[i] == 2016:
        végzett2016 += 1
print(f'{végzett2016} hallgató végzett 2016-ban.')

életkorok = [2014 - szül_dátum[i][0] for i in range(len(szül_dátum)) if kezdés[i] <= 2014 <= befejezés[i]]
átlag = 0
for i in range(len(életkorok)):
    átlag += életkorok[i]
print(f'Az átlag életkor {átlag/len(életkorok):.1f} év.')

