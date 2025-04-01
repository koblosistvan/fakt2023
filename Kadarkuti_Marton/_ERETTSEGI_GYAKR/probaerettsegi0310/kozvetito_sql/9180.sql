select kozterulet, hazszam, sum(case when funkcio = "terasz" then 0.5*szel*hossz else szel*hossz end) as alapterulet
from helyiseg inner join ingatlan on helyiseg.ingatlanid = ingatlan.id
group by ingatlanid
having alapterulet > 180