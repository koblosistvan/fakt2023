select szemely.nev, count(*)
from szemely JOIN fordito on szemely.id = fordito.szemelyid join nyelv on fordito.nyelvid = nyelv.id
where nyelv.fnyelv like "magyar"
GROUP by fordito.szemelyid
order by COUNT(*) DESC
limit 1