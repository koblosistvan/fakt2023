ettol = input().strip().split(':')
eddig = input().strip().split(':')
ettolperc = int(ettol[0])*60 + int(ettol[1])
eddigperc = int(eddig[0])*60 + int(eddig[1])
if eddigperc >= ettolperc:
    print(eddigperc-ettolperc)
else:
    print(24*60-ettolperc+eddigperc)
