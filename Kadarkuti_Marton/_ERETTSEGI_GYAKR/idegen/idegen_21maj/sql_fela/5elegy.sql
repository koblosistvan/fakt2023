select nev
from kapcsolat inner join keverek on kapcsolat.keverekid = keverek.id
group by keverekid
order by count(*) desc