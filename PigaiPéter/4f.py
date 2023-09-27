szám = 5
oszto = 2
i = True
b = True
while i:
    if szám == oszto:
        i = False
    elif szám < oszto+1:
        print('A szám nem prím')
        break
    elif szám % oszto == 0 and szám != oszto:
        print('A szám nem prím')
        break
    else:
        oszto += 1
if i == False:
    print('A szám prím')


#intervallum = input('Add neg az intervallumot')
#interalsofelso = intervallum.split(' ')
#interalso = int(interalsofelso[0])
#interfelso = int(interalsofelso[1])