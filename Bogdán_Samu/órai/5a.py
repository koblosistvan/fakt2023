forras1 = open('5a-magasugras2.txt', mode='r', encoding='utf-8')
forras2 = open('5a-magasugras.txt', mode='r', encoding='utf-8')
tavalyi = []
idei = []
kul = []

for i in forras1:
    x = i.strip().split(';')
    tavalyi.append(int(x[0]))
    idei.append(int(x[1]))
    kul.append(abs(int(x[0]) - int(x[1])))


print(max(tavalyi))
print(max(idei))
print(min(tavalyi))
print(min(idei))
print(max(kul))
print(min(kul))

forras1.close()
forras2.close()
