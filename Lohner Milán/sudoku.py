konnyu=open('konnyu.txt', mode='r', encoding='utf-8')
kozepes=open('kozepes.txt', mode='r', encoding='utf-8')
nehez=open('nehez.txt', mode='r', encoding='utf-8')

konnyu9=''
kozepes9=''
nehez9=''


tartalom=konnyu.readlines()


for i in range(9):
    konnyu9 += tartalom[i]




print(konnyu9)

valaszt=(input('Könnyű, közepes vagy nehéz: '))





