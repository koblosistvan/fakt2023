forras = open('5a-magasugras2.txt', mode='r', encoding='utf-8')

tavalyi = []
idei = []

for i in forras:
    x = i.strip().split(';')
    tavalyi.append(int(x[0]))
    idei.append(int(x[1]))

print(max(tavalyi))
print(max(idei))
forras.close()
