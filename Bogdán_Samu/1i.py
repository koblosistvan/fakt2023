idő = input("Kérlek add meg az időpontot: ")
óra, perc = idő.split(":")

perc_alfa = perc * 6
óra_alfa = (óra % 12) * 30


