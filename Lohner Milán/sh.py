lista=open('utonevek.txt', encoding='utf-8')
utonevek=[]

magas='e, é, i, í, ö, ő, ü, ű'
mely='a, á, o, ó, u, ú'
vegyes='e, é, i, í, ö, ő, ü, ű, a, á, o, ó, u, ú'



for sor in lista:
    adat=sor.strip().split('\n')
    utonevek.append(adat[0])
print(utonevek)

vezeteknev=input(':')
lehetnek=[]

for i in range(len(utonevek)):
    if len(utonevek[i]) + len(vezeteknev) >=15:
        lehetnek.append(utonevek)
print(lehetnek)


def hangrend(vezeteknev):
    hangrendek=''
    szaml1 = 0
    szaml2 = 0
    for i in vezeteknev:
        if i in magas:
            szaml1 += 1
        if i in mely:
            szaml2 +=1
        if szaml1 > 0 and szaml2==0:
            hangrendek+='magas'
        elif szaml1 == 0 and szaml2 > 0:
            hangrendek += 'magas'
        elif szaml1>0 and szaml2>0:
            hangrendek += 'vegyes'


for i in range(len(utonevek)):
    if hangrend(vezeteknev)==hangrend(utonevek[i]):
        lehetnek.append(utonevek[i])












