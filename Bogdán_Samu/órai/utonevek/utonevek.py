def hangrend(név):
    mélység = 0
    for i in range(len(név)):
        if név[i] in magas:
            if mélység == 0:
                mélység = 'magas'
            elif mélység == 'mély':
                mélység = 'vegyes'
                return mélység
        elif név[i] in mély:
            if mélység == 0:
                mélység = 'mély'
            elif mélység == 'magas':
                mélység = 'vegyes'
                return mélység
    return mélység
            
            
x = open('Bogdán_Samu\\órai\\utonevek\\utonevek.txt', 'r', encoding='utf-8')
y = open('Bogdán_Samu\\órai\\utonevek\\nevek.txt', 'w', encoding='utf-8')
vnév = input('> ')
magas = 'eéiíöőüűEÉIÍÖŐÜŰ'
mély = 'aáoóuúAÁOÓUÚ'
mélység1 = hangrend(vnév)
for e in x:
    mélység2 = 0
    knév = e.strip()
    if len(knév) + len(vnév) <= 30:
        mélység2 = hangrend(knév)
        if mélység1 == mélység2:
            y.write(f'{vnév} {knév}'+'\n')  
x.close()
y.close()