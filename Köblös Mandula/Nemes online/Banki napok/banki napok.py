forrás = open("banki napok.txt", mode="r", encoding="utf-8")

forrás.readline()

dolgozó = []
nap = []

for sor in forrás:
    adat = sor.strip().split(" ")
    dolgozó.append(int(adat[0]))
    nap.append(int(adat[1]))

forrás.close()

print("a.feladat")
dolgozó_kód = set(dolgozó)
for dolgozó_id in dolgozó_kód:
    print(f'Az {dolgozó_id} dolgozó {dolgozó.count(dolgozó_id)} alkalommal lépett be.')

print("b.feladat")
mindeketten = []
egyedül = []
for nap_id in set(nap):
    print(f"{nap_id}.nap:", end=" ")
    belépő = 0
    for dolgozó_id in dolgozó_kód:
        belépések = 0
        for i in range(len(dolgozó)):
            if dolgozó[i] == dolgozó_id and nap[i] == nap_id:
                belépések += 1
        print(belépések, end=" ")
        if belépések > 0:
            belépő += 1
    print()
    if belépő == len(set(dolgozó)):
        mindeketten.append(str(nap_id))
    if belépő < len(set(dolgozó)):
        egyedül.append(str(nap_id))
print("c.feladat")
print(f'Az {", ".join(mindeketten)} napokon léptek be mindektten.')
print(f'Az {", ".join(egyedül)} napokon nem léptek be mindektten')