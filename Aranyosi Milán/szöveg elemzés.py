def darab(szoveg):
    kijelento_db = szoveg.count('.')
    felszolito_db = szoveg.count('!')
    kerdo_db = szoveg.count('?')
    print(str(felszolito_db + kerdo_db + kijelento_db))
    print(felszolito_db)
    print(kijelento_db)
    print(kerdo_db)

darab('amjugy? nasidnas. nasdkasnd k! asndkasndk.')