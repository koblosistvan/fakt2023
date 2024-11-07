x = input('> ')
y = []
for i in range(len(x.strip().split(','))):
    a = x.strip().split(',')
    y.append(a[i][::-1])
print(f"> {','.join(y)}")