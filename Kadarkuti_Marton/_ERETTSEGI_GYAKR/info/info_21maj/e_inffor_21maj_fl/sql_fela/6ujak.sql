select helyezes, nev, cim
from lista inner join dalok on lista.dalid = dalok.dalid inner join eloadok on dalok.eloadoid = eloadok.eloadoid
where 
dalok.dalid in 
(
select dalid from lista where ev = 2019
)
and
dalok.dalid not in 
(
select dalid from lista where ev = 2018
)
order by helyezes asc