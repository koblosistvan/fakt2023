SELECT ingatlan.kozterulet, ingatlan.hazszam, hirdetes.ar 
from ingatlan JOIN hirdetes on ingatlan.id = hirdetes.ingatlanid 
where hirdetes.ar in (SELECT hirdetes.ar from hirdetes group by hirdetes.ingatlanid having hirdetes.allapot like "meghirdetve")