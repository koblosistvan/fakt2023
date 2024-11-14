k =open('Kerubina.txt' , encoding='utf-8')

t =open('Triton.txt' , encoding='utf-8')

kerubina=[]
triton=[]

for sor in k:
    adat = sor.strip().split('\n')
    kerubina.append(adat[0])

for sor in t:
    adat = sor.strip().split('\n')
    triton.append(adat[0])

sorszam=0

for i in range(len(kerubina)-1):
    j=0
    while j<len(triton) and kerubina[i] != triton[j]:
        j=j+1
    
