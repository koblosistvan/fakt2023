szavak1=open('szavak1.txt', encoding='utf-8')
szavak2=open('szavak2.txt', encoding='utf-8')

lszavak1=[]
lszavak2=[]

for sor in szavak1:
    adat=sor.strip().split('\n')
    lszavak1.append(adat[0])


for sor in szavak2:
    adat=sor.strip().split('\n')
    lszavak2.append(adat[0])

metszet=[]
sorszam=0

for i in range(len(lszavak1)-1):
    j=0
    while j<len(lszavak2) and lszavak1[i] != lszavak2[j]:
        j+=1
    if j < len(lszavak2):
       metszet.append(lszavak1[i])
       sorszam=sorszam+1


print(metszet)



