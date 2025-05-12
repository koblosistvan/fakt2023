SELECT ingatlan.kozterulet, ingatlan.hazszam, min(hirdetes.datum)
from ingatlan join hirdetes on ingatlan.id = hirdetes.ingatlanid
where hirdetes.allapot like "meghirdetve"