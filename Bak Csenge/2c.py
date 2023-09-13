a = 5
b = 8

if a*b > 30:
    print(f"Ez egy {a*b} m2-es nagy szoba.")
elif a*b > 10:
    print(f"Ez egy {a*b} m2-es közepes szoba.")
else:
    print(f"Ez egy {a*b} m2-es kicsi szoba.")

cs_a = 0.2
cs_b = 0.4
cs_szám = a*b / (cs_a * cs_b)
cs_maradék = a*b % (cs_a * cs_b)
if cs_maradék == 0:
    print(f"{cs_szám} csempére lesz szükség.")
else:
    print("Nem burkolható le egész csempékkel.")

print(f"{round(((cs_szám / 10) + cs_szám) / 12 + 0.5, 0)} dobozt kell rendelnünk.")







