def fact(n):
    if (n==1):
        return 1
    else:
        return fact(n-1)*n

def palindrome(txt: str):
    if (len(txt) in (0, 1)):
        return True
    else:
        if (txt[0]==txt[-1] and palindrome(txt[1:-1])):
            return True
        else:
            return False
        
def power(a:float, k:int):
    if (k<0):
        return 1 / power(a,-k)
    elif (k==0):
        return 1
    elif (k==1):
        return a
    elif (k%2==1):
        return power(a,k-1)*a
    else:
        return power(a,k//2)**2

def ncr(n:int, k:int):
    if (k in (0,n)):
        return 1
    elif (n==0):
        return 0
    else:
        return ncr(n-1,k-1) + ncr(n-1,k)

def pascal(nth_row):
    out = ""
    for i in range(nth_row+1):
        out += str(ncr(nth_row,i))
    return out