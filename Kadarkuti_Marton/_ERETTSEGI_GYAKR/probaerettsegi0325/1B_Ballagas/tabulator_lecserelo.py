with open("Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\probaerettsegi0325\\1B_Ballagas\\valaszok_igazi.txt",'w',encoding="utf-8") as x:
    f = open("Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\probaerettsegi0325\\1B_Ballagas\\valaszok.txt",'r',encoding="utf-8")
    for i in f:
        x.write('\t'.join(i.split(';')))