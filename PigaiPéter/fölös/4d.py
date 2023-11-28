pontok = open('../pontok.txt', mode='r', encoding='utf-8')

r = 0.5
xkord = []
ykord = []
pontokszáma = 0
for i in pontok:
    pontxy = i.split()
    xkord.append(float(pontxy[0]))
    ykord.append(float(pontxy[1]))
    if xkord[0] < r and ykord[0] < r:
        pontokszáma += 1
print(f'{pontokszáma} pont van a körvanalon belül')