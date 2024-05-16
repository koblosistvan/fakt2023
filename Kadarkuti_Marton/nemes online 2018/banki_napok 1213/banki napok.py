alkalmazott = []
nap = []
mindketto = []
with open("banki napok.txt","r",encoding="utf-8") as f:
    f.readline()
    for sor in f:
        data = list(map( int, sor.strip().split(" ")))
        alkalmazott.append(data[0])
        nap.append(data[1])
#print(alkalmazott)
#print(nap)

# 1.
elso_belepesek_szama = 0
for i in range(len(alkalmazott)):
    if alkalmazott[i] == 1:
        elso_belepesek_szama += 1

print("\n*1.")
print(f"Az egyik alkalmazott {elso_belepesek_szama} alkalommal lépett be,")
print(f"a másik {len(alkalmazott)-elso_belepesek_szama} alkalommal.")

# 2.
print("\n*2.")
naponta_data = []   # naponta hányszor
for _ in range(5):
    naponta_data.append([])

for i in range(len(nap)):
    naponta_data[nap[i]-1].append(alkalmazott[i])
for i in range(len(naponta_data)):
    if len(naponta_data[i]) != 0:
        print(f"{i+1}. napon {len(naponta_data[i])} belépés történt.")

# 3.
print("\n*3.")
harmas_feladat_boolean = False
for i in range(len(naponta_data)):
    if len(set(naponta_data[i])) > 1:
        harmas_feladat_boolean = True
        break
if harmas_feladat_boolean:
    print("Volt olyan nap, amikor mindkét dolgozó belépett.")
else:
    print("Nem volt olyan nap, amikor mindkét dolgozó belépett.")

# 4.
print("\n*4. ")
nem_lepett_be = 0
for i in range(len(naponta_data)):
    if len(set(naponta_data[i])) == 0:
        nem_lepett_be += 1
print(f"{nem_lepett_be} olyan nap volt, amikor egyik alkalmazott sem lépett be.")