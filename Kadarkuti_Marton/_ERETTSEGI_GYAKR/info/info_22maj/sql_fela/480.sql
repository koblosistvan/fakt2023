select nev, tipus, tav
from hely inner join allomas on hely.allomasid = allomas.id
where mukodo and vonalid = "80"
order by tav