select nev, count(*) as tavolmaradasok
from jelentkezes inner join diak on jelentkezes.diakid = diak.id
where elfogadva and not teljesitve
group by diakid
having tavolmaradasok >= 2