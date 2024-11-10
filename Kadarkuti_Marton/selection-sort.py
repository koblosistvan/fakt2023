import random

# selection sort
# atlagosan O(n^2)

N:int = 10
lista:list[int] = [random.randint(0,10) for _ in range(N)]
print("--- EREDETI---")
print(lista,'\n')

for i in range(N-1):
    min = i
    for j in range(i+1,N):
        if lista[j]<lista[min]:
            min = j
    
    lista[i], lista[min] = lista[min], lista[i]

print("--- RENDEZETT ---")
print(lista)