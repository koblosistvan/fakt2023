forras=open('lista.txt', mode='r', encoding='utf-8')


sorozatok=[]


for sor in forras:
    adat=sor.strip().split('\n')
    sorozatok.append(adat[0])


print(sorozatok)

nemismert = 0


for i in range(len(sorozatok)):
    if 'NI' in sorozatok[i]:
        nemismert += 1

print(nemismert)

vandatum=len(sorozatok)-nemismert
print(vandatum)

