szavak=input(':')

ujszavak=[]


for i in range(len(szavak)):
    ujszavak += chr(ord(szavak[i][::-1]))
print(szavak.join(ujszavak))
