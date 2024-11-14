import random

# Ezt a listát fogjuk rendezni.
számlista = [ random.randint(0, 100) for _ in range(10) ]
print(f'{számlista=}')

# Rendezés új listába:
másik_lista = sorted(számlista)
print(f'{másik_lista=}')

# Rendezés új listába, visszafelé:
másik_lista = sorted(számlista, reverse=True)
print(f'{másik_lista=}')

# Rendezés helyben:
számlista.sort()
print(f'{számlista=}')

# Rendezés helyben, visszafelé:
számlista.sort(reverse=True)
print(f'{számlista=}')

# Szöveg rendezése:
szöveglista = [sor.strip() for sor in open('_Megoldások/Összetett algoritmusok/Kerubina.txt', mode='r', encoding='utf-8')]
print('-'*50, '\nNyers szöveg')
print('\n'.join(szöveglista))

másik_lista = sorted(szöveglista)
print('-'*50, '\nRendezett szöveg')
print('\n'.join(másik_lista))

# Rendezés a nyelvi szabályok figyelembevételével
import locale
# A lokációt kiolvassuk az operációs rendszer beállításaiból
locale.setlocale(locale.LC_ALL, "")
# Másik lehetőség a lokáció kézzel történő beállítása,
# de magának a lokációnak ilyenkor is telepítve kell lennie a gépre.
# locale.setlocale(locale.LC_ALL, "hu_HU.UTF-8")

másik_lista = sorted(szöveglista, key=locale.strxfrm)
print('-'*50, '\nJól rendezett szöveg')
print('\n'.join(másik_lista))

# Rendezés valami más szabály szerint
másik_lista = sorted(szöveglista, key=lambda a: len(a))
print('-'*50, '\nHossz szerint')
print('\n'.join(másik_lista))

