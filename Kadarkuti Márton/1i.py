ido = input("Add meg az időpontot: ")
ora, perc = ido.split(":")

ora, perc = int(ora), int(perc)

kis_alfa = perc * 6
nagy_alfa = (ora % 12) * 30

print(f'{ora}:{perc}-kor a két mutató között {abs(nagy_alfa - kis_alfa)} fokos szög van')