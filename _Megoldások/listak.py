gyümölcsök = ['alma', 'körte', 'banán', 'cseresznye', 'meggy', 'füge']

print(gyümölcsök)
print(gyümölcsök[0])
print(gyümölcsök[2:4])
print(gyümölcsök[2:])
print(gyümölcsök[:3])
print(gyümölcsök[-4])
print(gyümölcsök[-3:])
print(len(gyümölcsök))

gyümölcsök[0] = 'szilva'
gyümölcsök.append('alma')
print(gyümölcsök)

a = 'blabla'
b = list('blabla')

print(a[1])
print(b[1])
