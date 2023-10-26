a = int(input('első szám:'))
b = int(input('utolsó szám:'))
#+
c = int(input('hányasával számoljon:'))
for i in range(a, b+1, c):
    print(i)