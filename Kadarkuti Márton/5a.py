# HF 0928: 5b

adat = open("5a-magasugras2.txt", mode="r", encoding="utf-8")

tavaly = []
idén = []

for i in adat:
    a = i.strip().split(";")
    tavaly.append(int(a[0]))
    idén.append(int(a[1]))
adat.close()

def vonal():
    print("-"*50)

száznyolcvan_felett = [0,0,0] #tavaly, idén, mindkettő

if len(tavaly) == len(idén):
    len = len(tavaly)
for i in range(len):
    b_tavaly = False
    b_idén = False
    if tavaly[i] > 180:
        száznyolcvan_felett[0] += 1
        b_tavaly = True
    if idén[i] > 180:
        száznyolcvan_felett[1] += 1
        b_idén = True
    if b_tavaly and b_idén:
        száznyolcvan_felett[2] += 1
print(f"\n{száznyolcvan_felett[0]} versenyző ugrott 180cm felett <tavaly>.")
print(f"{száznyolcvan_felett[1]} versenyző ugrott 180cm felett <idén>.")
print(f"{száznyolcvan_felett[2]} versenyző ugrott 180cm felett <mindkét évben>.")
vonal()

javitott = 0
for i in range(len):
    if tavaly[i] < idén[i]:
        javitott += 1
print(f"{javitott} versenyző javított a tavalyi eredményéhez képest.")
vonal()

szelsoertek_tavaly = [0,0]  #min, max
szelsoertek_idén = [0,0]

#tavaly
max = 0
min = 1000
for i in range(len):
    if max < tavaly[i]:
        max = tavaly[i]
    if min > tavaly[i]:
        min = tavaly[i]

szelsoertek_tavaly[0], szelsoertek_tavaly[1] = min, max

#idén
max = 0
min = 1000
for i in range(len):
    if max < idén[i]:
        max = idén[i]
    if min > idén[i]:
        min = idén[i]

szelsoertek_idén[0], szelsoertek_idén[1] = min, max

print(f"<Tavaly> a legmagasabb eredmény {szelsoertek_tavaly[1]}cm, a legalacsonyabb {szelsoertek_tavaly[0]}cm,")
print(f"<Idén> a legmagasabb eredmény {szelsoertek_idén[1]}cm, a legalacsonyabb {szelsoertek_idén[0]}cm volt.")
vonal()

a = 0
max = 0
min = 1000
for i in range(len):
    a = abs(idén[i] - tavaly[i])
    if a < min:
        min = a
    if a > max:
        max = a
print(f"A <legnagyobb változás> két év eredménye között {max}cm,")
print(f"A <legkisebb változás> két év eredménye között {min}cm volt.")
vonal()