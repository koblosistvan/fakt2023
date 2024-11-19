ferfinev = open('ferfi_nevek_eredete.txt', encoding='utf-8')
noinev = open('noi_nevek_eredete.txt', encoding='utf-8')


ferfilist = []
noilist = []
ferfieredet=[]
noieredet=[]

for sor in ferfinev:
    adat=sor.strip().split(',')
    ferfilist.append(adat[0])
    ferfieredet.append(adat[1])

for sor in noinev:
    adat=sor.strip().split(',')
    noilist.append(adat[0])
    noieredet.append(adat[1])


ferfinev.close()
noinev.close()



def NevKivalaszt(nevlista, kezdőbetű, maxhossz, eredete):
    jok=[]
    for i in range(len(nevlista)):
        if eredete in nevlista and nevlista[i][0]==kezdőbetű and len(nevlista[i])==maxhossz:
            jok.append(nevlista[i])
            return jok












