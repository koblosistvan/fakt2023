import math

hossz = float(input('Add meg a szoba szelesseget m-ben:  '))

szeles = float(input('Add meg a szoba hosszusagat m-ben: '))

terulet = hossz*szeles

csempek_dobozonkent = 12

csempe_szelesseg = float(input("Kerlek add meg a csempe szelességét meterben: "))
csempe_hossz = float(input("Kerlek add meg a csempe hosszat meterben: "))

veszt = 10

csempek_szama = (terulet * (1 + veszt / 100)) / (csempe_szelesseg * csempe_hossz)




if terulet > 30:
    print('Ez egy',terulet,'m2 -es nagyszoba')

elif 10<=terulet<=30:
    print('Ez egy',terulet,'-es kozepes szoba')

else:
    print('Ez egy',terulet,"m2 es kis szoba")


if csempek_szama.is_integer():
    print(f"A burkolashoz {int(csempek_szama)} csempe kell ")

else:
    print(f"{int(csempek_szama) + 1} csempe szukseges hogy lehetove tegyuk a szoba burkolasat.")

szukseges_dobozok = math.ceil(csempek_szama / csempek_dobozonkent)

print(f"A burkolashoz {szukseges_dobozok} doboz csempet kell rendelni.")