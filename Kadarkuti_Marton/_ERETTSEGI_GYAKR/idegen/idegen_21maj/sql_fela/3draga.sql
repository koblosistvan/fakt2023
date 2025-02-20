select nev, ar/tomeg *1000 as tomeg_kg
from keverek
order by tomeg_kg desc
limit 1