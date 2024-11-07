

dobasok=[3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4]

tart = 0
for i in range(len(dobasok)):
    tart += dobasok[i]
    if tart % 10==0:
        tart -= 3
    print(tart)





if tart > 45:
    print('A játékot befejezte')





