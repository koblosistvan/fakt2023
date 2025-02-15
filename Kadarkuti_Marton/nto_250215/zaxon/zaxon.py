

"""
N = int(f.readline())
nevek = []
for _ in range(N):
    nevek.append(f.readline().strip())
"""

N = int(input())
nevek = []
for _ in range(N):
    nevek.append(input())


def teszt():
    for _ in range(nevek.count(None)):
        nevek.remove(None)
    if len(nevek) == 0:
        print("Nincs")
        quit()
    elif len(nevek) == 1:
        print(nevek[0])
        quit()

#print("init:",nevek)
for n in range(N):
    if len(nevek[n]) < 5:
        nevek[n] = None
    elif len(set(nevek[n])) != len(nevek[n]):
        nevek[n] = None
#print("hossz szuro:",nevek)
teszt()

#print(min(nevek,key=len))
min = len(min(nevek,key=len))
for n in range(len(nevek)):
    if len(nevek[n]) != min:
        nevek[n] = None
teszt()
#print("hossz szuro 2:",nevek)
nevek.sort()
#print("sort:",nevek)
print(nevek[-1])

