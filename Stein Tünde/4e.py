szöveg = input('Szöveg: ')
magánhangzók = 'aáeéiíoóöőuúüű'
magánhangzók_a_szövegben = 0
gy = 0

for i in range(len(szöveg)):
    if szöveg[i].lower() in (magánhangzók):
        magánhangzók_a_szövegben += 1
for i in range(len(szöveg)-1):
    if szöveg[i].lower() == 'g' and szöveg[i+1].lower() == 'y':
        gy += 1
print(f'A magánhangzók száma a szövegben: {magánhangzók_a_szövegben}\nA gy betűk száma a szövegben: {gy}')
