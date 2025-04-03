select szemely.nev
from fordito inner join szemely on fordito.szemelyid = szemely.id inner join nyelv on fordito.nyelvid = nyelv.id
where nyelv.fnyelv = "magyar"
group by fordito.szemelyid
order by count(distinct nyelv.cnyelv) desc
limit 1