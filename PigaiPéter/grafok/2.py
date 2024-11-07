import random
csucsok = list(range(10))
elek = []
for i in csucsok:
    elek.append([])
for el in range(15):
    elek[random.randint(0, 9)].append(random.randint(0, 9))

print(f'{csucsok}')
print(f'{elek}')

stack = [0]
visited = [False] * len(csucsok)
while len(stack):
    vizsgalt = stack.pop()
    if not visited[vizsgalt]:
        visited[vizsgalt] = True
        for i in elek[vizsgalt]:
            stack.append(i)

print(visited)

stack = [0]
visited = [False] * len(csucsok)

def rekurziv(v):
    visited[v] = True
    for i in elek[v]:
        if not visited[i]:
            return rekurziv(v)

