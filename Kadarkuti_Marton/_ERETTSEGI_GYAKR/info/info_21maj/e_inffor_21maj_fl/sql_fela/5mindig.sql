select nev, cim
from dalok inner join eloadok on dalok.eloadoid = eloadok.eloadoid
where dalid in 
(
select distinct dalid from lista
group by dalid
having count(*)=21
)