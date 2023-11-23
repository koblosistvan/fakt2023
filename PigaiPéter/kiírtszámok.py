mondat = '21 121 benyó balázs'
szavak = mondat.split(' ')
egy = 'egy'
kettő = 'kettő'
három = 'három'
négy = 'négy'
őt = 'öt'
hat = 'hat'
hét = 'hét'
nyolc = 'nyolc'
kilenc = 'kilenc'
tíz = 'tíz'
tizen = 'tizen'
húsz = 'húsz'
huszon = 'huszon'
harmic = 'harminc'
negyven = 'negyven'
ötven = 'ötven'
hatvan ='hatvan'
hetven = 'hetven'
nyolcvan = 'nyolcvan'
kilencven = 'kilencven'



for i in szavak:
    if (type(i) == float or type(i) == int) and int(i) < 100:
        szám = [i.split('')]
        for j in szám:
            if int(j) < 10:

