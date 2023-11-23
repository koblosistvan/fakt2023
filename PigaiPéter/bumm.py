mettől = int(input('Mettől?'))
meddig = int(input('Meddig?'))
tiltott = int(input('Tiltott'))

számsor = []

for i in range(mettől, meddig + 1):
    számjegyek = [x for x in str(i)]
    print(számjegyek)
    if i < 10:
        if i == tiltott or i % tiltott == 0:
            számsor.append('!!')
        else:
            számsor.append(i)
    else:
        if i == tiltott or i % tiltott == 0 or int(számjegyek[0]) == tiltott or int(számjegyek[1]) == tiltott:
            számsor.append('!!')
        else:
            számsor.append(i)

print(számsor)