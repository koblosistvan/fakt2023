
tol = input().strip().split(':')
ig = input().strip().split(':')
tol = 60*int(tol[0]) + int(tol[1])
ig = 60*int(ig[0]) + int(ig[1])

if tol > ig:
    ig += 24*60

print(abs(tol-ig))