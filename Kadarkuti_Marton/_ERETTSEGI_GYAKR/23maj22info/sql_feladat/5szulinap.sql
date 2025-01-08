select nev, szuldatum, datum
from alvas inner join diak on diak.id = alvas.diakid
where day(szuldatum) = day(datum) and month(szuldatum) = 9