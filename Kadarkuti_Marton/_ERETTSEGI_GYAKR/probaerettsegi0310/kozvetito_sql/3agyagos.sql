select hazszam, ar
from hirdetes inner join ingatlan on hirdetes.ingatlanid = ingatlan.id
where allapot = "meghirdetve" and kozterulet = "Agyagos utca"