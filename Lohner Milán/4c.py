forrás = open('4c-bolt.txt',mode='r',encoding='utf-8')

bevétel=[]
kiadás=[]

for sor in forrás:
    adat = sor.strip().split(',')
    bevétel.append(int(adat[0]))
    kiadás.append(int(adat[1]))
forrás.close()

print(bevétel)
print(kiadás)

sokbevétel = 0

for i in range(len(bevétel)):
    if bevétel[i] > kiadás[i] * 1.1:
        sokbevétel += 1

print(f'{sokbevétel} napon volt 10% al több a bevétel a kiadásnál')



veszteség=0

for i in range(len(bevétel)):
    if bevétel[i] < kiadás[i]:
        veszteség += 1

print(f'{veszteség} napon történt veszteség')

profit=0

for i in range(len(bevétel)):
    if bevétel[i] > kiadás[i]:

