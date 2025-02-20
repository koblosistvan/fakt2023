import rotatescreen as rs
import time
def fakt(n):
    if n == 1:
        return 1
    else:
        pd = rs.get_primary_display()
        a = [90, 180, 270, 0]
        for i in range(2):
            for x in a:
                pd.rotate_to(x)
                time.sleep(0.02)
        return fakt(n-1) * n
print(fakt(3))
