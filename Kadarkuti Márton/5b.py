import random
import math
def vonal():
    print("-"*30)


mérések = [] #  első: 0:30 ; utolsó: 24:00
c = 0
def görbe(x):
    return round(6*math.sin(x/12) + 18)   #18-15 között generál

for i in range(24*2):
    c = görbe(c)
    c = random.randint(c-1, c)
    mérések.append(c)
    c = i

#print(mérések)

l = len(mérések)

#+1   30°C felett
harminc_felett = 0
for i in range(l):
    if mérések[i] > 30:
        harminc_felett += 1
vonal()
print(f"{harminc_felett} alkalommal volt 30°C felett a hőmérséklet.")

#+2 átlag
c = 0
for i in range(l):
    c += mérések[i]
c = round(c/l)
vonal()
print(f"{c}°C az <átlaghőmérséklet>.")

#+3 csökkent/nőtt előzőhöz képest
nőtt = 0
csökkent = 0
for i in range(l-1):
    if mérések[i+1] > mérések[i]:
        nőtt += 1
    if mérések[i+1] < mérések[i]:
        csökkent += 1
vonal()
print(f"A hőmérséklet az előző fél órához képest {nőtt} alkalommal <nőtt>,")
print(f"és {csökkent} alkalommal <csökkent>.")

#+4 minimum, maximum
min = 40
max = 0
for i in range(l):
    if mérések[i] > max:
        max = i
    if mérések[i] < min:
        min = i

def órává_alakít(y):
    y = (y+1)/2
    if y.is_integer():
        y = round(y)
        y = str(y)
        y += ":00"
    else:
        y = math.floor(y)
        y = str(y)
        y += ":30"
    return y

vonal()
print(f"A <legmagasabb> mért hőmérséklet {mérések[max]}°C, {órává_alakít(max)} időpontban,")
print(f"A <legalacsonyabb> mért hőmérséklet {mérések[min]}°C, {órává_alakít(min)} időpontban.")

#+5 legnagyobb két mérés között
c = 0
max = 0
for i in range(l-1):
    c = abs(mérések[i] - mérések[i+1])
    if c > max:
        max = c
vonal()
print(f"A <legnagyobb eltérés> két egymást követő mérés között {max}°C.")
vonal()

print("     <ADATTÁBLA>")
for i in range(l):
    print(f"{órává_alakít(i)} időpontban {mérések[i]}°C")
vonal()
