össz = int(input().strip())
a = int(input().strip())
b = int(input().strip())

x = []
for i in range(össz//a+1):
    x.append([i, (össz-i*a)//b])

print(len(x))
for i in range(len(x)):
    print(' '.join(map(str, x[i])))