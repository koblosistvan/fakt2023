#2c feladat
import math

print("-A program kiszámolja egy adott téglalap alakú szoba területét négyzetméterben.-")
a = float(input("\n▶ Add meg a szoba vízszintes hosszát (m): "))
b = float(input("▶ Add meg a szoba függőleges hosszát (m): "))
l = [a,b]

def valid():
    global a
    global b
    if a <= 0 or b <= 0:
        print("\n:Érvénytelen a beírt érték:")
        quit()
    if a.is_integer() == True:
        a = int(a)
    if b.is_integer() == True:
        b = int(b)
valid()

print("")

print(f"Szélesség: {a} m")
print(f"Hosszúság: {b} m")

if a == b:
    print("[Négyzet]")
    v = a
    f = a
else:
    v = a
    f = b
    print("[Téglalap]")

terulet = round(a*b, 2)
if terulet == int(terulet):
    terulet = int(terulet)

if terulet < 10:
    subst = "kis"
if terulet >= 10 and terulet < 30:
    subst = "közepes"
if terulet >= 30:
    subst = "nagy"

#2c +1
print(f"Ez egy {terulet} m²-es {subst} szoba.")

#2c +2
print("\n-Burkolhatóság számoló-")
a = (float(input("▶ Add meg a csempe vízszintes hosszát (cm): "))) / 100
b = (float(input("▶ Add meg a csempe függőleges hosszát (cm): "))) / 100
l = [a,b]

valid()

print(f"Csempe kiterjedése: {100*a} cm × {100*b} cm.")

if a == b:
    print("[Négyzet alakú]")
    v_cs = a
    f_cs = a
else:
    v_cs = a
    f_cs = b
    print("[Téglalap alakú]")

t_cs = round(v_cs * f_cs, 1)

print("")

if terulet < t_cs:
    print("A csempe túl nagy.")
    print("")
    quit()

veszteseg = 1.1
doboz = 12


#vizszintes:
v_r = math.ceil(v / v_cs) * math.ceil(f / f_cs)
v_r = math.floor(v_r * veszteseg)
v_doboz = math.ceil(v_r / doboz)
print(f"Vízszintesen burkolva {math.floor(v_r)}db csempére van szükség.")
print(f"Ez minimum {v_doboz} doboz csempe.")

#függőleges:
f_r = math.ceil(f / v_cs) * math.ceil(v / f_cs)
f_r = math.floor(f_r * veszteseg)
f_doboz = math.ceil(f_r / doboz)
print(f"Függőlegesen burkolva {math.floor(f_r)}db csempére van szükség.")
print(f"Ez minimum {f_doboz} doboz csempe.")

print(f"\n* 1 doboz = {doboz}db csempét tartalmaz")
print(f"** hozzáadott {math.floor(veszteseg*100)}%-os veszteséggel együtt")
print("")
