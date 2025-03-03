n_m = input().split(' ')
n = int(n_m[0])
m = int(n_m[1])
lanc = [0]*n
hiba = False
for i in range(m):
    meres = input().split(' ')
    sorszam = int(meres[0])
    reszlet = meres[1]
    for k in range(len(reszlet)):
        if not lanc[sorszam-1] or lanc[sorszam-1] == reszlet[k]:
            lanc[sorszam-1] = reszlet[k]
            sorszam += 1
        elif lanc[sorszam-1]:
            hiba = True
for i in range(n):
    if not lanc[i]:
        lanc[i] = '?'
if not hiba:
    print(*lanc, sep='')
else:
    print('Hiba!')

