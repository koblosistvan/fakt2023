select distinct kozterulet, hazszam, ar
from hirdetes inner join ingatlan on hirdetes.ingatlanid = ingatlan.id
where ingatlanid in 
(
select m.ingatlanid
from hirdetes as m, hirdetes as e
where m.allapot = "meghirdetve" and e.allapot = "eladva"
and m.ingatlanid = e.ingatlanid and m.ar = e.ar
)