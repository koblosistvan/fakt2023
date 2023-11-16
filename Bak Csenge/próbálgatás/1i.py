#idő = input("Kérlek add meg az időpontot: ")
idő = "02:15"

óra, perc = idő.split(":")
óra = int(óra)
perc = int(perc)

kis_afa = perc/60 * 360
nagy_alfa = (óra % 12) / 12 * 360

print(f"{óra}:{perc}-kor a két mutató között {abs(nagy_alfa - kis_afa)} fokos szög van.")







