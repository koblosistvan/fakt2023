import json
f = open("Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\info\\info_21maj\\e_inffor_21maj_fl\\evszam\\sorok_data.json",'r',encoding="utf-8")

f = f.read()
f = json.loads(f)

alt = 0

# csak txt
with open("Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\info\\info_21maj\\e_inffor_21maj_fl\\evszam\\ez_nem_script_"+str(alt)+".txt",'w',encoding="utf-8") as x:
    for i in f:
        x.write(i[1]+'\t\n')
alt+=1

# ev + txt
with open("Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\info\\info_21maj\\e_inffor_21maj_fl\\evszam\\ez_nem_script_"+str(alt)+".txt",'w',encoding="utf-8") as x:
    for i in f:
        x.write(i[0] + '\t'+ i[1] +'\t\n')
alt+=1

# txt + [""]
with open("Kadarkuti_Marton\\_ERETTSEGI_GYAKR\\info\\info_21maj\\e_inffor_21maj_fl\\evszam\\ez_nem_script_"+str(alt)+".txt",'w',encoding="utf-8") as x:
    for i in f:
        x.write(i[1]+'\t[""]\n')
alt+=1
