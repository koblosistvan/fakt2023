import math
sz_x = int(input("Adja meg a szoba szélességét (m): "))
sz_y = int(input("Adja meg a szoba hosszát (m): "))
terulet = sz_x * sz_y
if terulet > 30:
    print(f"Ez egy {terulet} m^2-es nagy szoba.")
elif 10 <= terulet <= 30:       # todo: code review
    print(f"Ez egy {terulet} m^2-es közepes szoba.")
else:
    print(f"Ez egy {terulet} m^2-es kis szoba.")

cs_x = int(input("Adja meg a csempe szélességét (m): "))
cs_y = int(input("Adja egy a csempe hosszát (m): "))
csempe = cs_x * cs_y
if (sz_x % cs_x == 0 and sz_y % cs_y == 0) or (sz_x % cs_y == 0 and sz_y % cs_x == 0): # todo: code review
    print("A szoba leburkolható egész csempékkel.")
    print(f" A szoba leburkolásához {math.ceil(terulet / csempe)} darab csempére + 10% veszteségként {math.ceil((terulet / csempe) * 0.1)} darab csempére lesz szükség.")
else:
    print("A szoba nem burkolható le egész csempékkel.")

doboz = math.ceil(math.ceil((terulet / csempe) * 1.10) / 12)
print(f"{doboz} doboz csempét kell rendelni a szoba teljes leburkolásához.")
