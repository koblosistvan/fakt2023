import random
a = sorted([random.randint(1,20) for _ in range(10)])
print(a)

bal=0
jobb=len(a)-1

def binker(keresett, bal, jobb):
    if jobb < bal:
        return -1
    else:
        kozep = (bal+jobb)//2
        if a[kozep] == keresett:
            return kozep
        elif keresett < a[kozep]:
            return binker(keresett, bal, kozep-1)
        else:
            return binker(keresett, kozep+1, jobb)

print(binker(3,bal,jobb))