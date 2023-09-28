forrás = open('5a-magasugras2.txt', mode='r', encoding='utf-8')

tavaly = []
idén = []

for sor in forrás:
    adat = sor.strip().split(';')
    tavaly.append(int(adat[0]))
    idén.append(int(adat[1]))

forrás.close()


idei_max_id = 0
idei_max_magasság = idén[0]

for i in range(1, len(idén)):
    if idén[i] > idei_max_magasság:
        idei_max_magasság = idén[i]
        idei_max_id = i

print(f'A legmagasabbat idén a {idei_max_id}. sportoló ugrotta: {idei_max_magasság} cm.')