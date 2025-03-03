 SELECT keverek.nev, (1000/keverek.tomeg) * keverek.ar
from keverek
order by (1000/keverek.tomeg) * keverek.ar DESC
limit 1