hivas_szám, percek = [int(s) for s in input().split()]
hívások = [int(s) for s in input().split()]

vége = max(hívások)
dolgozó = 0
max_dolgozó = 0
for i in range(vége+1):
    dolgozó += hívások.count(i) # a bejövőhöz kell plusz ember
    dolgozó -= hívások.count(i-percek) # ennyit tesznek le
    if dolgozó > max_dolgozó:
        max_dolgozó = dolgozó

print(max_dolgozó)

'''
teszt 1
3 2
1 2 3

teszt 2
4 1
1 1 2 3

teszt 3
3 3
1 2 3

'''