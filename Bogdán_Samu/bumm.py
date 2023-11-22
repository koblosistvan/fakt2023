forrás = input('bumm(ettől,eddig,tiltott): ')
ettől = int(forrás.split(',')[0])
eddig = int(forrás.split(',')[1])
tiltott = int(forrás.split(',')[2])
for i in range(ettől, eddig+1):
    if str(tiltott) in str(i) or i % tiltott == 0:
        print('!!', end=' ')
    else:
        print(i, end=' ')
