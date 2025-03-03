select nev, tav
from hely inner join allomas on hely.allomasid = allomas.id
where 
vonalid = "140"
and
tav <= 100