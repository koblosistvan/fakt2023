intervallum = input('Add meg két számot kiszámolom közöttük a prímeket:').split(' ')
a = int(intervallum[0])
b = int(intervallum[1])



def príme(szam):
    prim = True
    for i in range(2, round(szam / 2) + 1):
      if szam % i == 0:
         prim = False
         break
    return prim


primek_szama = 0
for i in range(a, b+1):
    if príme(i):
        primek_szama += 1
print(f'Az {intervallum} intervallumban {primek_szama} prím szám van.')
