alap = input('> ')
kodolt = ''
for i in alap:
    if ord(i) < (ord('z') - 2):
        kodolt += chr(ord(i)+3)
    elif ord('a') <= ord(i) <= ord('z'):
        kodolt += chr(  ord('a')+(ord(i)-ord('z')+2)  )
    elif ord(i) < (ord('Z') - 2):
        kodolt += chr(ord(i)+3)
    elif ord('A') <= ord(i) <= ord('Z'):
        kodolt += chr(  ord('A')+(ord(i)-ord('Z')+2)  )
print(kodolt)
