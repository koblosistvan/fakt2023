
ido=input('Add meg az időpontot')
ora, perc=ido.split(':')
ora=int(ora)
perc=int(perc)

kis_alfa = perc * 6
nagy_alfa = (ora % 12) / 12 * 36
print(f'{ora}:{perc}-kor a két mutató között {abs(nagy_alfa - kis_alfa)} fokos szög van')