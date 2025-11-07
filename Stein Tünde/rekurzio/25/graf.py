def teljesel(n):
    if n == 1:
        return 0
    else:
        return teljesel(n-1) + n-1
print(teljesel(4))