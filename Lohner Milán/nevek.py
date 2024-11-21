forras1 =open('top100utonev_2011.txt', encoding='utf-8')
forras2 =open('top100utonev_2021.txt', encoding='utf-8')

top2011nevek=[]
top2021nevek=[]



for sor in forras1:
    adat=sor.strip().split('\t')
    top2011nevek.append(adat[0])
    top2011nevek.append(adat[1])
    top2011nevek.append(adat[2])
    top2011nevek.append(adat[3])

for sor in forras2:
    adat=sor.strip().split('\t')
    top2021nevek.append(adat[0])
    top2021nevek.append(adat[1])
    top2021nevek.append(adat[2])
    top2021nevek.append(adat[3])


forras1.close()
forras2.close()






both=[]
sorszám = 0
for i in range(len(top2011nevek)-1):
    max = i
    for j in range(i+1, len(top2021nevek)):
        if int(top2021nevek)



print(both)














