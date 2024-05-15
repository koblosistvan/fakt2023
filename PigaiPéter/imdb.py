class Filmek:
    def __init__(self, ev: int, idotartam: int, ertekeles: float, rendezo: str, bevetel: int, cim: str):
        self.ev = ev
        self.idotartam = idotartam
        self.ertekeles = ertekeles
        self.rendezo = rendezo
        self.bevetel = bevetel
        self.cim = cim


forras = open('PigaiPéter\\imdb.txt', mode='r', encoding='utf-8')
imdb = []
forras.readline()
for sor in forras:
    adat = sor.strip().split('\t')
    imdb.append(Filmek(ev=int(adat[0]), idotartam=int(adat[1]), ertekeles=float(adat[2]), rendezo=str(adat[3]), bevetel=int(adat[4]), cim=str(adat[5])))
forras.close

#1
print(f'{len(imdb)} van összesen')

#2
legkisebb = imdb[0].ev
for i in imdb:
    if legkisebb > i.ev:
        legkisebb = i.ev
print(f'{legkisebb} évben jött ki a legrégebbi film')

#
hoszabb = 0
for i in imdb:
    if i.idotartam > 120:
        hoszabb += 1
if hoszabb == 0:
    print('Nincs két óránál hosszabb film.')
else:
    print(f'{hoszabb} db 2 óránál hoszabb film van')

#
van = False
for i in imdb:
    if i.ertekeles > 9:
        van = True
        break
if van == True:
    print('Van 9-es értékelésnél magasabb film')
else:
    print('Nincs 9-es értékelésnél magasabb film')

#
legmagasabb = imdb[0].ertekeles
for i in imdb:
    if i.ertekeles > legmagasabb:
        legmagasabb = i.ertekeles
print(f'A legmagasabb értékeles:{legmagasabb}')

#
átkozott = input('átkozott???:')
if átkozott == 'igen':
    a0 = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    a11 = 0
    a12 = 0
    a13 = 0
    a14 = 0
    a15 = 0
    a16 = 0
    a17 = 0
    a18 = 0
    a19 = 0
    a20 = 0
    a21 = 0
    a22 = 0
    a23 = 0
    a24 = 0
    a25 = 0
    a26 = 0
    a27 = 0
    a28 = 0
    a29 = 0
    a30 = 0
    a31 = 0
    a32 = 0
    a33 = 0
    a34 = 0
    a35 = 0
    a36 = 0
    a37 = 0
    a38 = 0
    a39 = 0
    a40 = 0
    a41 = 0
    a42 = 0
    a43 = 0
    a44 = 0
    a45 = 0
    a46 = 0
    a47 = 0
    a48 = 0
    a49 = 0
    a50 = 0
    a51 = 0
    a52 = 0
    a53 = 0
    a54 = 0
    a55 = 0
    a56 = 0
    a57 = 0
    a58 = 0
    a59 = 0
    a60 = 0
    a61 = 0
    a62 = 0
    a63 = 0
    a64 = 0
    a65 = 0
    a66 = 0
    a67 = 0
    a68 = 0
    a69 = 0
    a70 = 0
    a71 = 0
    a72 = 0
    a73 = 0
    a74 = 0
    a75 = 0
    a76 = 0
    a77 = 0
    a78 = 0
    a79 = 0
    a80 = 0
    a81 = 0
    a82 = 0
    a83 = 0
    a84 = 0
    a85 = 0
    a86 = 0
    a87 = 0
    a88 = 0
    a89 = 0
    a90 = 0
    a91 = 0
    a92 = 0
    a93 = 0
    a94 = 0
    a95 = 0
    a96 = 0
    a97 = 0
    a98 = 0
    a99 = 0
    for i in imdb:
        if i.ertekeles == 9.9:
            a99 += 1
        elif i.ertekeles == 0.0:
                    a0 += 1
        elif i.ertekeles == 0.1:
                a1 += 1
        elif i.ertekeles == 0.2:
                a2 += 1
        elif i.ertekeles == 0.3:
                a3 += 1
        elif i.ertekeles == 0.4:
                a4 += 1
        elif i.ertekeles == 0.5:
                a5 += 1
        elif i.ertekeles == 0.6:
                a6 += 1
        elif i.ertekeles == 0.7:
                a7 += 1
        elif i.ertekeles == 0.8:
                a8 += 1
        elif i.ertekeles == 0.9:
                a9 += 1
        elif i.ertekeles == 1.0:
                a10 += 1
        elif i.ertekeles == 1.1:
                a11 += 1
        elif i.ertekeles == 1.2:
                a12 += 1
        elif i.ertekeles == 1.3:
                a13 += 1
        elif i.ertekeles == 1.4:
                a14 += 1
        elif i.ertekeles == 1.5:
                a15 += 1
        elif i.ertekeles == 1.6:
                a16 += 1
        elif i.ertekeles == 1.7:
                a17 += 1
        elif i.ertekeles == 1.8:
                a18 += 1
        elif i.ertekeles == 1.9:
                a19 += 1
        elif i.ertekeles == 2.0:
                a20 += 1
        elif i.ertekeles == 2.1:
                a21 += 1
        elif i.ertekeles == 2.2:
                a22 += 1
        elif i.ertekeles == 2.3:
                a23 += 1
        elif i.ertekeles == 2.4:
                a24 += 1
        elif i.ertekeles == 2.5:
                a25 += 1
        elif i.ertekeles == 2.6:
                a26 += 1
        elif i.ertekeles == 2.7:
                a27 += 1
        elif i.ertekeles == 2.8:
                a28 += 1
        elif i.ertekeles == 2.9:
                a29 += 1
        elif i.ertekeles == 3.0:
                a30 += 1
        elif i.ertekeles == 3.1:
                a31 += 1
        elif i.ertekeles == 3.2:
                a32 += 1
        elif i.ertekeles == 3.3:
                a33 += 1
        elif i.ertekeles == 3.4:
                a34 += 1
        elif i.ertekeles == 3.5:
                a35 += 1
        elif i.ertekeles == 3.6:
                a36 += 1
        elif i.ertekeles == 3.7:
                a37 += 1
        elif i.ertekeles == 3.8:
                a38 += 1
        elif i.ertekeles == 3.9:
                a39 += 1
        elif i.ertekeles == 4.0:
                a40 += 1
        elif i.ertekeles == 4.1:
                a41 += 1
        elif i.ertekeles == 4.2:
                a42 += 1
        elif i.ertekeles == 4.3:
                a43 += 1
        elif i.ertekeles == 4.4:
                a44 += 1
        elif i.ertekeles == 4.5:
                a45 += 1
        elif i.ertekeles == 4.6:
                a46 += 1
        elif i.ertekeles == 4.7:
                a47 += 1
        elif i.ertekeles == 4.8:
                a48 += 1
        elif i.ertekeles == 4.9:
                a49 += 1
        elif i.ertekeles == 5.0:
                a50 += 1
        elif i.ertekeles == 5.1:
                a51 += 1
        elif i.ertekeles == 5.2:
                a52 += 1
        elif i.ertekeles == 5.3:
                a53 += 1
        elif i.ertekeles == 5.4:
                a54 += 1
        elif i.ertekeles == 5.5:
                a55 += 1
        elif i.ertekeles == 5.6:
                a56 += 1
        elif i.ertekeles == 5.7:
                a57 += 1
        elif i.ertekeles == 5.8:
                a58 += 1
        elif i.ertekeles == 5.9:
                a59 += 1
        elif i.ertekeles == 6.0:
                a60 += 1
        elif i.ertekeles == 6.1:
                a61 += 1
        elif i.ertekeles == 6.2:
                a62 += 1
        elif i.ertekeles == 6.3:
                a63 += 1
        elif i.ertekeles == 6.4:
                a64 += 1
        elif i.ertekeles == 6.5:
                a65 += 1
        elif i.ertekeles == 6.6:
                a66 += 1
        elif i.ertekeles == 6.7:
                a67 += 1
        elif i.ertekeles == 6.8:
                a68 += 1
        elif i.ertekeles == 6.9:
                a69 += 1
        elif i.ertekeles == 7.0:
                a70 += 1
        elif i.ertekeles == 7.1:
                a71 += 1
        elif i.ertekeles == 7.2:
                a72 += 1
        elif i.ertekeles == 7.3:
                a73 += 1
        elif i.ertekeles == 7.4:
                a74 += 1
        elif i.ertekeles == 7.5:
                a75 += 1
        elif i.ertekeles == 7.6:
                a76 += 1
        elif i.ertekeles == 7.7:
                a77 += 1
        elif i.ertekeles == 7.8:
                a78 += 1
        elif i.ertekeles == 7.9:
                a79 += 1
        elif i.ertekeles == 8.0:
                a80 += 1
        elif i.ertekeles == 8.1:
                a81 += 1
        elif i.ertekeles == 8.2:
                a82 += 1
        elif i.ertekeles == 8.3:
                a83 += 1
        elif i.ertekeles == 8.4:
                a84 += 1
        elif i.ertekeles == 8.5:
                a85 += 1
        elif i.ertekeles == 8.6:
                a86 += 1
        elif i.ertekeles == 8.7:
                a87 += 1
        elif i.ertekeles == 8.8:
                a88 += 1
        elif i.ertekeles == 8.9:
                a89 += 1
        elif i.ertekeles == 9.0:
                a90 += 1
        elif i.ertekeles == 9.1:
                a91 += 1
        elif i.ertekeles == 9.2:
                a92 += 1
        elif i.ertekeles == 9.3:
                a93 += 1
        elif i.ertekeles == 9.4:
                a94 += 1
        elif i.ertekeles == 9.5:
                a95 += 1
        elif i.ertekeles == 9.6:
                a96 += 1
        elif i.ertekeles == 9.7:
                a97 += 1
        elif i.ertekeles == 9.8:
                a98 += 1
        elif i.ertekeles == 9.9:
                a99 += 1
    print(f"{a0} db film kapott 0.0-es értékelést")
    print(f"{a1} db film kapott 0.1-es értékelést")
    print(f"{a2} db film kapott 0.2-es értékelést")
    print(f"{a3} db film kapott 0.3-es értékelést")
    print(f"{a4} db film kapott 0.4-es értékelést")
    print(f"{a5} db film kapott 0.5-es értékelést")
    print(f"{a6} db film kapott 0.6-es értékelést")
    print(f"{a7} db film kapott 0.7-es értékelést")
    print(f"{a8} db film kapott 0.8-es értékelést")
    print(f"{a9} db film kapott 0.9-es értékelést")
    print(f"{a10} db film kapott 1.0-es értékelést")
    print(f"{a11} db film kapott 1.1-es értékelést")
    print(f"{a12} db film kapott 1.2-es értékelést")
    print(f"{a13} db film kapott 1.3-es értékelést")
    print(f"{a14} db film kapott 1.4-es értékelést")
    print(f"{a15} db film kapott 1.5-es értékelést")
    print(f"{a16} db film kapott 1.6-es értékelést")
    print(f"{a17} db film kapott 1.7-es értékelést")
    print(f"{a18} db film kapott 1.8-es értékelést")
    print(f"{a19} db film kapott 1.9-es értékelést")
    print(f"{a20} db film kapott 2.0-es értékelést")
    print(f"{a21} db film kapott 2.1-es értékelést")
    print(f"{a22} db film kapott 2.2-es értékelést")
    print(f"{a23} db film kapott 2.3-es értékelést")
    print(f"{a24} db film kapott 2.4-es értékelést")
    print(f"{a25} db film kapott 2.5-es értékelést")
    print(f"{a26} db film kapott 2.6-es értékelést")
    print(f"{a27} db film kapott 2.7-es értékelést")
    print(f"{a28} db film kapott 2.8-es értékelést")
    print(f"{a29} db film kapott 2.9-es értékelést")
    print(f"{a30} db film kapott 3.0-es értékelést")
    print(f"{a31} db film kapott 3.1-es értékelést")
    print(f"{a32} db film kapott 3.2-es értékelést")
    print(f"{a33} db film kapott 3.3-es értékelést")
    print(f"{a34} db film kapott 3.4-es értékelést")
    print(f"{a35} db film kapott 3.5-es értékelést")
    print(f"{a36} db film kapott 3.6-es értékelést")
    print(f"{a37} db film kapott 3.7-es értékelést")
    print(f"{a38} db film kapott 3.8-es értékelést")
    print(f"{a39} db film kapott 3.9-es értékelést")
    print(f"{a40} db film kapott 4.0-es értékelést")
    print(f"{a41} db film kapott 4.1-es értékelést")
    print(f"{a42} db film kapott 4.2-es értékelést")
    print(f"{a43} db film kapott 4.3-es értékelést")
    print(f"{a44} db film kapott 4.4-es értékelést")
    print(f"{a45} db film kapott 4.5-es értékelést")
    print(f"{a46} db film kapott 4.6-es értékelést")
    print(f"{a47} db film kapott 4.7-es értékelést")
    print(f"{a48} db film kapott 4.8-es értékelést")
    print(f"{a49} db film kapott 4.9-es értékelést")
    print(f"{a50} db film kapott 5.0-es értékelést")
    print(f"{a51} db film kapott 5.1-es értékelést")
    print(f"{a52} db film kapott 5.2-es értékelést")
    print(f"{a53} db film kapott 5.3-es értékelést")
    print(f"{a54} db film kapott 5.4-es értékelést")
    print(f"{a55} db film kapott 5.5-es értékelést")
    print(f"{a56} db film kapott 5.6-es értékelést")
    print(f"{a57} db film kapott 5.7-es értékelést")
    print(f"{a58} db film kapott 5.8-es értékelést")
    print(f"{a59} db film kapott 5.9-es értékelést")
    print(f"{a60} db film kapott 6.0-es értékelést")
    print(f"{a61} db film kapott 6.1-es értékelést")
    print(f"{a62} db film kapott 6.2-es értékelést")
    print(f"{a63} db film kapott 6.3-es értékelést")
    print(f"{a64} db film kapott 6.4-es értékelést")
    print(f"{a65} db film kapott 6.5-es értékelést")
    print(f"{a66} db film kapott 6.6-es értékelést")
    print(f"{a67} db film kapott 6.7-es értékelést")
    print(f"{a68} db film kapott 6.8-es értékelést")
    print(f"{a69} db film kapott 6.9-es értékelést")
    print(f"{a70} db film kapott 7.0-es értékelést")
    print(f"{a71} db film kapott 7.1-es értékelést")
    print(f"{a72} db film kapott 7.2-es értékelést")
    print(f"{a73} db film kapott 7.3-es értékelést")
    print(f"{a74} db film kapott 7.4-es értékelést")
    print(f"{a75} db film kapott 7.5-es értékelést")
    print(f"{a76} db film kapott 7.6-es értékelést")
    print(f"{a77} db film kapott 7.7-es értékelést")
    print(f"{a78} db film kapott 7.8-es értékelést")
    print(f"{a79} db film kapott 7.9-es értékelést")
    print(f"{a80} db film kapott 8.0-es értékelést")
    print(f"{a81} db film kapott 8.1-es értékelést")
    print(f"{a82} db film kapott 8.2-es értékelést")
    print(f"{a83} db film kapott 8.3-es értékelést")
    print(f"{a84} db film kapott 8.4-es értékelést")
    print(f"{a85} db film kapott 8.5-es értékelést")
    print(f"{a86} db film kapott 8.6-es értékelést")
    print(f"{a87} db film kapott 8.7-es értékelést")
    print(f"{a88} db film kapott 8.8-es értékelést")
    print(f"{a89} db film kapott 8.9-es értékelést")
    print(f"{a90} db film kapott 9.0-es értékelést")
    print(f"{a91} db film kapott 9.1-es értékelést")
    print(f"{a92} db film kapott 9.2-es értékelést")
    print(f"{a93} db film kapott 9.3-es értékelést")
    print(f"{a94} db film kapott 9.4-es értékelést")
    print(f"{a95} db film kapott 9.5-es értékelést")
    print(f"{a96} db film kapott 9.6-es értékelést")
    print(f"{a97} db film kapott 9.7-es értékelést")
    print(f"{a98} db film kapott 9.8-es értékelést")
    print(f"{a99} db film kapott 9.9-es értékelést")
else:
    ertekelesek = set()
    for i in imdb:
           ertekelesek.add(i.ertekeles)
    ertekelesek = 
    print(ertekelesek)