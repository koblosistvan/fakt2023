set @osszes = (select letszam from megye where nev = "Pest");
select sum(letszam)/@osszes as pesten_reszt_vett
from aerob
where mkod = (select kod from megye where nev = "Pest")