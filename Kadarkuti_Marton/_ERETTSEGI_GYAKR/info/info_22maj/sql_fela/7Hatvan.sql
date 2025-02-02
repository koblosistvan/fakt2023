-- (select id from allomas where nev = "Hatvan")
-- 1976
select nev, vonalid
from hely inner join allomas on hely.allomasid = allomas.id
where
nev != "Hatvan"
AND
vonalid in (select vonalid from hely inner join allomas on hely.allomasid = allomas.id where nev = "Hatvan")