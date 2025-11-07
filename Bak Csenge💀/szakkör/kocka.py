forrás = open("kocka.graf", mode="r", encoding="utf-8")

gráf = []

for sor in forrás:
    adat = sor.strip().split("\t")
    gráf.append(adat)

forrás.close()

bekért = input("Add meg az útvonalat. ").split(" ")

for i in range(len(bekért)-1):
    lista = [bekért[i], bekért[i+1]]
    if lista not in gráf:
        print("Nem járható be")
        break
else:
    print("Bejárható")


