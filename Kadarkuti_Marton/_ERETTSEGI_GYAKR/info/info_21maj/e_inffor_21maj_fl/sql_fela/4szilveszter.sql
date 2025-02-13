select helyezes, nev, cim
from lista inner join dalok on lista.dalid = dalok.dalid inner join eloadok on dalok.eloadoid = eloadok.eloadoid
where ev = 2019 and helyezes <= 285
order by helyezes asc