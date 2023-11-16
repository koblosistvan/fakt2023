forrás = open("5a-magasugras2.txt", mode="r", encoding="utf-8")

tavaly = []
idén = []

for sor in forrás:
    adat = sor.strip(). split(";")
    tavaly.append(int(adat[0]))
    idén.append(int(adat[1]))

forrás.close()




idei_max = idén[0]
idei_max_id = 0
idei_min = idén[0]
idei_min_id = 0
tavalyi_max = idén[0]
tavalyi_max_id = 0
tavalyi_min = idén[0]
tavalyi_min_id = 0

legkisebb_válltozás = abs(idén[0] - tavaly[0])
legnagyobb_válltozás = -1


for i in range(1, len(tavaly)):
    if idei_max < idén[i]:
        idei_max = idén[i]
        idei_max_id = i
    if idei_min > idén[i]:
        idei_min = idén[i]
        idei_min_id = i
    if tavalyi_max < idén[i]:
        tavalyi_max = idén[i]
        tavalyi_max_id = i
    if tavalyi_min > idén[i]:
        tavalyi_min = idén[i]
        tavalyi_min_id = i
    if abs(idén[i] - tavaly[i]) < legkisebb_válltozás:
        legkisebb_válltozás = abs(idén[i] - tavaly[i])
    if abs(idén[i] - tavaly[i]) > legnagyobb_válltozás:
        legnagyobb_válltozás = abs(idén[i] - tavaly[i])

print(f"legnagyobb tavaly: {max(tavaly)} {tavalyi_max_id=}")
print(f"legkisebb tavaly: {min(tavaly)} {tavalyi_min_id=}")
print(f"legnagyobb idén: {max(idén)} {idei_max_id=}")
print(f"legkisebb idén: {min(idén)} {idei_min_id=}")
print(f"{legnagyobb_válltozás=}")
print(f"{legkisebb_válltozás=}")


