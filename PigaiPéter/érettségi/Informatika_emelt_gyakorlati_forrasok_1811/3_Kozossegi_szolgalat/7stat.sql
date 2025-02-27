select diak.osztaly ,count(diak.id)
from diak
where diak.id in (SELECT diakid from jelentkezes where jelentkezes.teljesitve)
group by diak.osztaly