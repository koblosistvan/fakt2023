szöveg = str(input("Írd be a szöveget: "))

mgh = ['a','A','á','Á','e','E','é','É','i','I','í','Í','o','O','ó','Ó','ö','Ö','ő','Ő','u','U','ú','Ú','ü','Ü','ű','Ű']
magánhangzó = 0
gy_számláló = 0

G = ['g', 'G']
Y = ['y', 'Y']
for i in range(len(szöveg)):
    if szöveg[i] in mgh:
        magánhangzó += 1
for i in range(len(szöveg) -1 ):

    if szöveg[i] in G and szöveg[i+1] in Y:
        gy_számláló += 1


    elif (szöveg[i] in G) and (szöveg[i+1] in G) and (szöveg[i+2] in Y):
        gy_számláló += 1
        i += 1

print(f"\n   # A szövegben {magánhangzó} darab magánhangzó,")
print(f"   # és {gy_számláló} 'gy' betű van.")