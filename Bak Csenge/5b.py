forrás = open("5b-homerseklet.txt", mode="r", encoding="utf-8")

h_min = []
fok = []

for sor in forrás:
    adat = sor.strip().split("\t")
    h_min.append(adat[0])
    fok.append(float(adat[1]))

forrás.close()

#1. feladat
print(f"Beolvastam {len(fok)} rekordot")

harminc_felett = 0

for i in range(len(fok)):
    if fok[i] > 30:
        harminc_felett += 1

print(f"A nap folyamán {harminc_felett} alkalommal mértünk 30°C-nál nagyobb hőmérsékletet.")

nőtt = 0
csökk = 0

for i in range(1, len(fok)):
    if fok[i-1] < fok[i]:
        nőtt += 1
    if fok[i-1] > fok[i]:
        csökk += 1

print(f"{nőtt} alkalommal nőtt és {csökk} alkalommal csökkent a hőmérséklet az előző méréshez képest.")

max_hő = fok[0]
max_hő_id = 0

min_hő = fok[0]
min_hő_id = 0

for i in range(len(fok)):
    if fok[i] > max_hő:
        max_hő = fok[i]
        max_hő_id = i
    if fok[i] < min_hő:
        min_hő = fok[i]
        min_hő_id = i

print(f"A legalacsonyabb hőmérsékletet {h_min[min_hő_id]}-kor mértük és {min_hő}°C volt.\nA legmagasabb hőmérsékletet {h_min[max_hő_id]}-kor mértük és {max_hő}°C volt.")

emelkedés = 0
emelkedés_id = []

for i in range(1, len(fok)):
    if fok[i] - fok[i-1] > emelkedés:
        emelkedés = fok[i] - fok[i-1]
        emelkedés_id = [i-1, i]

print(f"A legnagyobb emelkedés {h_min[emelkedés_id[0]]}-{h_min[emelkedés_id[1]]} között volt: {fok[emelkedés_id[0]]}°C - {fok[emelkedés_id[1]]}°C = {round(emelkedés, 2)}°C")

seged_szamitas = 0
leggyanúsabb = [fok[0], fok[1], fok[2]]
leggyanúsabb_id = 0

for i in range(1, len(fok)-1):
    if abs((fok[i-1] + fok[i+1] / 2) - fok[i]) > seged_szamitas:
        seged_szamitas = (fok[i-1] + fok[i+1] / 2) - fok[i]
        leggyanúsabb = [fok[i-1], fok[i], fok[i+1]]
        leggyanúsabb_id = i

print(f"A leggyanúsabb mérést {h_min[leggyanúsabb_id]}-kor mértük: {leggyanúsabb[0]}, {leggyanúsabb[1]}, {leggyanúsabb[2]}")



