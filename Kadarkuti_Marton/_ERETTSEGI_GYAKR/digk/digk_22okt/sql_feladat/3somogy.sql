select sum(letszam) as somogy_megye_letszam
from aerob
where mkod = (SELECT kod from megye where nev = "Somogy")