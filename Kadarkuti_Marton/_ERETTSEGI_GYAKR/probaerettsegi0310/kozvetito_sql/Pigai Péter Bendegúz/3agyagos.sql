select ingatlan.hazszam, hirdetes.ar
from ingatlan join hirdetes on ingatlan.id = hirdetes.ingatlanid
where ingatlan.kozterulet like "Agyagos utca"