forrás = input('bumm(ettől,eddig,tiltott): ')
def bumm(ettől,eddig,tiltott):
    for i in range(ettől, eddig+1):
        if str(tiltott) in list(str(i)) or i % tiltott == 0:
            print('!!')
        else:
            print(i)
bumm(int(forrás.split(',')[0]),int(forrás.split(',')[1]),int(forrás.split(',')[2]))