triton = open("PigaiPéter\Triton.txt", mode="r", encoding="utf-8")
kerubina = open("PigaiPéter\Kerubina.txt", mode="r", encoding="utf-8")
triton_halmaz = []
kerubina_halmaz = []
for sor in triton:
    triton_halmaz.append(sor.strip('\n'))
for sor in kerubina:
    kerubina_halmaz.append(sor.strip('\n'))
triton.close()
kerubina.close()
unio = []
# for i in range(len(triton_halmaz)):
    for j in range(len(kerubina_halmaz)):
        if triton_halmaz[j] == kerubina_halmaz[j]:
            unio.append(triton_halmaz[i])
            pass
print(unio)

