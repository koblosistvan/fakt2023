f1 = open("Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_22maj/Informatika_forras_E2211/4_Epitmenyado/"+"fizetendo-pugusz.txt",'r',encoding="utf-8")
f2 = open("Kadarkuti_Marton/_ERETTSEGI_GYAKR/info/info_22maj/Informatika_forras_E2211/4_Epitmenyado/"+"fizetendo.txt",'r',encoding="utf-8")

f1lista = []
f2lista = []

for i in range(520):
    f1lista.append(f1.readline().strip())
    f2lista.append(f2.readline().strip())

f1lista = sorted(list(set(f1lista)))
f2lista = sorted(list(set(f2lista)))
print(f1lista==f2lista)