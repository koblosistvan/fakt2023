def szo(n):
    if n<10:
        return n
    else:
        return n%10 + szo(n//10)