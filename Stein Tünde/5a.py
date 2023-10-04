forrás = open('5a-magasugras2.txt', mode='r', encoding='utf-8')
magasság_tavaly = []
magasság_idén = []
for sor in forrás:
    adat = sor.strip().split(';')
    magasság_tavaly.append(int(adat[0]))
    magasság_idén.append(int(adat[1]))

forrás.close()

print(f'{magasság_tavaly},\n{magasság_idén}')

idei_max_id = 0
idei_max_magasság = magasság_idén[0]
idei_min_id = 0
idei_min_magasság = magasság_idén[0]
tavalyi_max_id = 0
tavalyi_max_magasság = magasság_idén[0]
tavalyi_min_id = 0
tavalyi_min_magasság = magasság_idén[0]

for i in range(1, len(magasság_idén)):
    if magasság_idén[i] > idei_max_magasság:
        idei_max_magasság = magasság_idén[i]
        idei_max_id = i
    elif magasság_idén[i] < idei_min_magasság:
        idei_min_magasság = magasság_idén[i]
        idei_min_id = i
    elif magasság_tavaly[i] > tavalyi_max_magasság:
        tavalyi_max_magasság = magasság_tavaly[i]
        tavalyi_max_id = i
    elif magasság_tavaly[i] < tavalyi_min_magasság:
        tavalyi_min_magasság = magasság_tavaly[i]
        tavalyi_min_id = i
    if magasság_tavaly[i] > magasság_idén[i]:


print(f'{idei_max_id}: {idei_max_magasság}')