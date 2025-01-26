select distinct nev, vege.ut
from vege inner join telepules on vege.telepid = telepules.id
group by vege.ut,telepid
having count(vege.ut)=2