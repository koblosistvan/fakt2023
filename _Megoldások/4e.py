szöveg = input('Add meg a szöveget: ')
magánhangzók = 'aáeéiíoóöőuúüű'
magánhangzók_száma = 0

for i in range(len(szöveg)):
    if szöveg[i].lower() in magánhangzók:
        magánhangzók_száma += 1

print(magánhangzók_száma)