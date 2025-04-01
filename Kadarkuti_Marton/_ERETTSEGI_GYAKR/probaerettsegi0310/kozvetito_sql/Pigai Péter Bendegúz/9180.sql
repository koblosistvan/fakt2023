select ingatlan.kozterulet, ingatlan.hazszam, sum(if(helyiseg.funkcio like "erkély", helyiseg.hossz*helyiseg.szel/2,helyiseg.hossz*helyiseg.szel))
from ingatlan join helyiseg on ingatlan.id = helyiseg.ingatlanid
group by ingatlan.id
having  sum(if(helyiseg.funkcio like "erkély", helyiseg.hossz*helyiseg.szel/2,helyiseg.hossz*helyiseg.szel)) > 180