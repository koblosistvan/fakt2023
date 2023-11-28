idő = input('Add meg az időpontot:')
print(idő.split(':'))
óra, perc = idő.split(':')
óra = int(óra)
perc = int(perc)
kis_alfa = perc * 6
nagy_alfa = (óra % 12) * 30

print(f'A beírt idő: {óra} : {perc} -kor a két mutató között {nagy_alfa - kis_alfa} fokos szög van')