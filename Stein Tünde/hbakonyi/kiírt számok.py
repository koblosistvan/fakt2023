rage = range
mondat = input('> ')
mondatlista = []
for i in rage(mondat.count(' ')+1):
    mondatlista.append(mondat.strip().split(' ' or ', ')[i])      #csak szóközre működik, de azért ott hagyom
print(mondatlista)      #L>>szavakra bontom a listát :3

def szamok(x):      #www.youtube.com/watch?v=grXGH0KUVrU&list=PLTOsBXsSLoBm2tynrTSgNjm651N23p1rw&index=1
    if x == '0':
        x = ''
    elif x == '1':
        x = 'egy'
    elif x == '2':
        x = 'kettő'
    elif x == '3':
        x = 'három'
    elif x == '4':
        x = 'négy'
    elif x == '5':
        x = 'öt'
    elif x == '6':
        x = 'hat'
    elif x == '7':
        x = 'hét'
    elif x == '8':
        x = 'nyolc'
    elif x == '9':
        x = 'kilenc'
    return x

def atalakit(mondat):
    for i in rage(len(mondat)):
        try:
            mondat[i] = int(mondat[i])
            if mondat[i] < 100:
                if 0 <= mondat[i] <= 10 or mondat[i] == 20:
                    if mondat[i] == 0:
                        mondat[i] = 'nulla'
                    elif mondat[i] == 1:
                        mondat[i] = 'egy'
                    elif mondat[i] == 2:
                        mondat[i] = 'kettő'
                    elif mondat[i] == 3:
                        mondat[i] = 'három'
                    elif mondat[i] == 4:
                        mondat[i] = 'négy'
                    elif mondat[i] == 5:
                        mondat[i] = 'öt'
                    elif mondat[i] == 6:
                        mondat[i] = 'hat'
                    elif mondat[i] == 7:
                        mondat[i] = 'hét'
                    elif mondat[i] == 8:
                        mondat[i] = 'nyolc'
                    elif mondat[i] == 9:
                        mondat[i] = 'kilenc'
                    elif mondat[i] == 10:
                        mondat[i] = 'tíz'
                    elif mondat[i] == 20:
                        mondat[i] = 'húsz'
                else:
                    mondat[i] = str(mondat[i])
                    if mondat[i][0] == 1:
                        mondat[i][0] = 'tizen'
                        mondat[i][1] = szamok(mondat[i][1])
                    elif mondat[i][0] == 2:
                        mondat[i][0] = 'huszon'
                        mondat[i][1] = szamok(mondat[i][1])
                    elif mondat[i][0] == 3:
                        mondat[i][0] = 'harminc'
                        mondat[i][1] = szamok(mondat[i][1])
                    elif mondat[i][0] == 4:
                        mondat[i][0] = 'negyven'
                        mondat[i][1] = szamok(mondat[i][1])
                    elif mondat[i][0] == 5:
                        mondat[i][0] = 'ötven'
                        mondat[i][1] = szamok(mondat[i][1])
                    elif mondat[i][0] == 6:
                        mondat[i][0] = 'hatvan'
                        mondat[i][1] = szamok(mondat[i][1])
                    elif mondat[i][0] == 7:
                        mondat[i][0] = 'hetven'
                        mondat[i][1] = szamok(mondat[i][1])
                    elif mondat[i][0] == 8:
                        mondat[i][0] = 'nyolcvan'
                        mondat[i][1] = szamok(mondat[i][1])
                    elif mondat[i][0] == 9:
                        mondat[i][0] = 'kilencven'
                        mondat[i][1] = szamok(mondat[i][1])
            else:
                mondat[i] = str(mondat[i])
        except:
            continue
    return mondat

segedvaltozo = atalakit(mondatlista)
print(" ".join(segedvaltozo))