select kozterulet, hazszam, datum
from hirdetes inner join ingatlan on hirdetes.ingatlanid = ingatlan.id
where 
ingatlanid not in (select ingatlanid from hirdetes where allapot = "eladva" or allapot = "módosítva")
order by datum
limit 1