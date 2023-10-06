forrás = open('ajto.txt', mode='r', encoding='utf-8')

óra = []
perc = []
az = []
log = []
for i in forrás:
    sor = i.strip().split(' ')
    óra.append(int(sor[0]))
    perc.append(int(sor[1]))
    az.append(int(sor[2]))
    log.append(str(sor[3]))

index_be = []
index_ki = []
for i in range(len(log)):
    if log[i] == 'be':
        index_be.append(i)
    if log[i] == 'ki':
        index_ki.append(i)
index_be = index_be[0]
index_ki = index_ki[-1]
print(az[index_be], az[index_ki])

athaladas = open('athaladas.txt', mode='w', encoding='utf-8')
azonosító = list(dict.fromkeys(az))
azonosító.sort()
az_db = []
for i in azonosító:
    az_db.append(az.count(i))
for i in range(len(azonosító)):
    pass

forrás.close()
