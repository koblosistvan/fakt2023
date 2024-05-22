# 0.
tablazat = []
with open("Vtabla.dat", "r", encoding="utf-8") as f:
    for sor in f:
        tablazat.append( list( sor.strip() ) )

def vonal():
    print("-"*30)
def debugPrint():
    for i in range(26):
        print(tablazat[i])

debugPrint()

# 1.
print("EZAPROBASZOVEGAMITKODOLUNK")
while True:
    rawUserInput = input("[Bemenet] > ")
    if len(rawUserInput) > 255:
        print("A bemenet túl hosszú.")
        continue
    break

# 2.
# ékezetek kiszedése
EKEZET = list("ÁÉÍÓÖŐÚÜŰ")
JAV_EKEZET = list("AEIOOOUUU")

vonal()
bemenet = list(rawUserInput.upper())

for i in range(len(rawUserInput)):
    temp = bemenet[i]
    if temp in EKEZET:
        bemenet[i] = JAV_EKEZET[ EKEZET.index(temp) ]

# csak betűk maradnak
LATIN_ = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(len(bemenet)):
    if bemenet[i] not in LATIN_:
        bemenet[i] = None
for _ in range(bemenet.count(None)):
    bemenet.remove(None)

# 3.
print(*bemenet, sep="")

# 4. max 5 karakteres

vonal()
rawKulcsInput = input("\n[Kulcs] > ")
vonal()

rawKulcsInput = rawKulcsInput.upper()
kulcs = rawKulcsInput * (len(bemenet) // len(rawKulcsInput) + 1)
kulcs = kulcs[:len(bemenet)]
print(*bemenet, sep="")
print(kulcs)

# 5.
def hanyadik(betu): # A => 0; B => 1; ...
    return LATIN_.index(betu)


kimenet = bemenet.copy()
for i in range(len(bemenet)):
    kimenet[i] = tablazat[ hanyadik( bemenet[i] ) ][ hanyadik( kulcs[i] ) ]
print("")

vonal()
print("Enkódolt:")
print(*kimenet,sep="")

try:  # ha nincs kodolt.dat akkor csinál
    f = open("kodolt.dat", "x", encoding="utf-8")
    f.write("")
except:
    pass

with open("kodolt.dat", "a", encoding="utf-8") as f:  # beírja a fájlba az enkódolt szöveget
    kimenetStr = "".join( kimenet )
    f.write(f"{kimenetStr}\n")