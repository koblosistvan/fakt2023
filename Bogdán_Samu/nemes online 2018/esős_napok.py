napok_száma = int(input(''))
napok = list(input('').split(' '))
for i in range(len(napok)):
    napok[i] = int(napok[i])

print('a. feladat')
print(len(napok) - napok.count(0))

print('\n' + 'b. feladat')
száraz = []
x = 0
for i in range(len(napok)):
    if napok[i] == 0:
        x += 1
    elif napok[i] > 0:
        száraz.append(x)
        x = 0
print(max(száraz))

kétnap = []
for i in range(len(napok)-1):
    x = napok[i] + napok[i+1]
    kétnap.append(x)
print('\n' + 'c. feladat')
print(max(kétnap))
