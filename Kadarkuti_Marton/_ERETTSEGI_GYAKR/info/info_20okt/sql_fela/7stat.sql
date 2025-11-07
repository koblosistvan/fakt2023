select osztaly, count(distinct diakid)
from jelentkezes inner join diak on jelentkezes.diakid = diak.id
where diakid in (select diakid from jelentkezes where teljesitve)
group by osztaly