

k=1.0
a=1.0
for num in range(9999999):
     k = k + 2
     a = a - ( 1 / k ) + 1 / ( k + 2 )
     k = k + 2
print ( 4 * a ) 
    