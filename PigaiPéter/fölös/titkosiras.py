prompt = input("Szöveg:")
coded = []
for i in prompt:
    if  64 <  ord(i) < 91:
        coded.append(chr(ord(i)+3))
    elif ord(i)+3 > 90:
            coded.append(chr(64 + abs(90-ord(i)+3)))
    else:
        coded.append(i)
print(''.join(coded))