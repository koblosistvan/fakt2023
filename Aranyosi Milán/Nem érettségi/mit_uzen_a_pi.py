text_pi = '''
3.14159265358979323846264338327950288419716939937510582097494459
230781640628620899862803482534211706798214808651328230664709384
460955058223172535940812848111745028410270193852110555964462294
895493038196442881097566593344612847564823378678316527120190914
564856692346034861045432664821339360726024914127372458700660631
558817488152092096282925409171536436789259036001133053054882046
652138414695194151160943305727036575959195309218611738193261179
310511854807446237996274956735188575272489122793818301194912983
367336244065664308602139494639522473719070217986094370277053921
717629317675238467481846766940513200056812714526356082778577134
275778960917363717872146844090122495343014654958537105079227968
925892354201995611212902196086403441815981362977477130996051870
72113499999983729780499510597317328160963185950244594553469083
026425223082533446850352619311881710100031378387528865875332083
814206171776691473035982534904287554687311595628638823537875937
519577818577805321712268066130019278766111959092164201989380952
572010654858632788659361533818279682303019520353018529689957736
225994138912497217752834791315155748572424541506959508295331168
617278558890750983817546374649393192550604009277016711390098488
240128583616035637076601047101819429555961989467678374494482553
797747268471040475346462080466842590694912933136770289891521047
521620569660240580381501935112533824300355876402474964732639141
992726042699227967823547816360093417216412199245863150302861829
745557067498385054945885869269956909272107975093029553211653449
872027559602364806654991198818347977535663698074265425278625518
184175746728909777727938000816470600161452491921732172147723501
41441973568548161361157352552133475741849468438523323907394143334
5477624168625189835694855620992192221842725502542568876717904
946016534668049886272327917860857843838279679766814541009538837
863609506800642251252051173929848960841284886269456042419652850
222106611863067442786220391949450471237137869609563643719172874
677646575739624138908658326459958133904780275901
'''
'''
nulla = 0
egy = 0
ketto = 0
harom = 0
negy = 0
ot = 0
hat = 0
het = 0
nyolc = 0
kilenc = 0

for i in text_pi:
    if i == '0':
        nulla += 1
    if i == '1':
        egy += 1
    if i == '2':
        ketto += 1
    if i == '3':
        harom += 1
    if i == '4':
        negy += 1
    if i == '5':
        ot += 1
    if i == '6':
        hat += 1
    if i == '7':
        het += 1
    if i == '8':
        nyolc += 1
    if i == '9':
        kilenc += 1


szamok.append(nulla)
szamok_index.append('0')
szamok.append(egy)
szamok_index.append('1')
szamok.append(ketto)
szamok_index.append('2')
szamok.append(harom)
szamok_index.append('3')
szamok.append(negy)
szamok_index.append('4')
szamok.append(ot)
szamok_index.append('5')
szamok.append(hat)
szamok_index.append('6')
szamok.append(het)
szamok_index.append('7')
szamok.append(nyolc)
szamok_index.append('8')
szamok.append(kilenc)
szamok_index.append('9')
'''

szamok = [] #előfurdulások számának listája

szamok_index = [] #melyik szájegyhez tartozik az előfordulási érték

for i in range(0, 10): #ciklussal 0-tól 9-ig számok
    szamok_index.append(str(i))

for j in range(len(szamok_index)):
    i_szaml = 0
    for i in text_pi:
        if i == szamok_index[j]:
            i_szaml += 1
    szamok.append(i_szaml)

for i in range(len(szamok)-1):
    legnagyobb = i
    for j in range(i+1, len(szamok)):
        if szamok[j] > szamok[legnagyobb]:
            legnagyobb = j
    seged = szamok[i]
    szamok[i] = szamok[legnagyobb]
    szamok[legnagyobb] = seged

    seged_ketto = szamok_index[i]
    szamok_index[i] = szamok_index[legnagyobb]
    szamok_index[legnagyobb] = seged_ketto

for i in range(len(szamok)):
    print(f'A(z) {i+1:2}. leggyakoribb számjegy a "{int(szamok_index[i])}" volt {szamok[i]} előfordulással.')

szamkod = ''

for i in range(len(szamok_index)):
    szamkod += szamok_index[i]

print(f'A kapott számkód: {szamkod}')
