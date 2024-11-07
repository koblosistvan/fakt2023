mondat = input('Add meg a mondatot: ')

ujmondat=[]

for i in range(len(mondat)):
    ujmondat += chr(ord(mondat[i])+3)


print(ujmondat)