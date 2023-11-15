idő = input('Kérlek add meg az időpontot: ')
ora, perc =idő.split(':')

ora = int(ora)
perc = int(perc)

kis_alfa = perc * 6
nagy_alfa = (ora % 12) * 30

print(f'{ora}:{perc}-kor a két mutató között {abs(kis_alfa - nagy_alfa)} fokos szög van')