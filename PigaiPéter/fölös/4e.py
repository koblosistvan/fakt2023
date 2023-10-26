szöveg = input(':')
maganhangzo = 'aáeéiíuúüűoóöőAÁEÉIÍOÓÖUÚÜŰ'
mgszövegbe = 0
gymennyiseg = 0
for i in range(len(szöveg)):
    if szöveg[i] in maganhangzo:
        mgszövegbe += 1
for i in range(len(szöveg)-1):
    if szöveg[i] in ('g', 'G') and szöveg[i+1] in 'y':
        gymennyiseg += 1
print(mgszövegbe)
print(gymennyiseg)
