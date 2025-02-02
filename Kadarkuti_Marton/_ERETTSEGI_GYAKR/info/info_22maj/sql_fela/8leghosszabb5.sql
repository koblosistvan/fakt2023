select nev, count(vonalid) as vonalak_szama
from hely inner join allomas on hely.allomasid = allomas.id
group by allomasid
having vonalak_szama >= 5
order by vonalak_szama desc