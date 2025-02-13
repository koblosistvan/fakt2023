select ev as "Év", helyezes as "Helyezés", nev as "Előadó", cim as "Dal", megjelenes as "Megjelenés"
from lista inner join dalok on lista.dalid = dalok.dalid inner join eloadok on dalok.eloadoid = eloadok.eloadoid
where helyezes between 1 and 10
order by ev, helyezes