ido = input("Add meg az időpontot: ")
ora, perc = ido.split(":")

ora, perc = int(ora), int(perc)

kalfa = perc * 6
nalfa = (ora % 12) * 30

print(f'{ora}{perc}-kor a két mutató közöztti szög {abs(nalfa-kalfa)} lesz')