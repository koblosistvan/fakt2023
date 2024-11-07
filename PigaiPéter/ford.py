prompt = input("Szöveg:")
reverse = []
for i in range(len(prompt)):
    reverse.append('')
a = 0
for i in prompt:
    reverse[len(prompt)-a-1] = i
    a += 1
print(''.join(reverse))