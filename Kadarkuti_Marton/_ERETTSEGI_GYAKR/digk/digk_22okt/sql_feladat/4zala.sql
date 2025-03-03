select sum(letszam)
from aerob
where 
nem
and
mkod = (select kod from megye where nev = "Zala")
AND
allkod = (select kod from allapot where nev = "egészséges")