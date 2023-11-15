# A program kérje be a burkoláshoz használt csempe méreteit,
# majd számolja ki, hogy leburkolható-e egész csempékkel.

szoba_szélesség = int(input('Add meg a szoba szélességét: '))
szoba_hossz = int(input('Add meg a szoba hosszát: '))

csempe_a = int(input('Add meg a csempe egyik méretét: '))
csempe_b = int(input('Add meg a csempe másik méretét: '))

# akkor burkolható le egész csempékkel, ha a szoba egyik mérete osztható a csempe
# egyik oldalának hosszával, a másik pedig a másikkal

if ((szoba_hossz % csempe_a == 0) and (szoba_szélesség % csempe_b == 0)) \
    or ((szoba_hossz % csempe_b == 0) and (szoba_szélesség % csempe_a == 0)):
    eredmény = 'leburkolható'
else:
    eredmény = 'nem burkolható le'

print(f'A {szoba_hossz}x{szoba_szélesség} méretű szoba '
      f'{eredmény} {csempe_a}x{csempe_b} méretű egész csempékkel.')
