f = open("valaszok_regi.txt",'r',encoding="utf-8")
x = open("valaszok.txt",'w',encoding="utf-8")
x.write(f.readline())

for i in f:
    sor = i.strip().split('@iskola.hu')
    sor[0] = sor[0].split('.')
    sor[0] = sor[0][0].capitalize() + ' ' + sor[0][1].capitalize()
    x.write(sor[0]+sor[1]+'\n')