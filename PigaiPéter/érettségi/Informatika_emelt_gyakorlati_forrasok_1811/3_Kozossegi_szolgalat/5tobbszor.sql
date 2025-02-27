select diak.nev, count(jelentkezes.ervenyes)+count(jelentkezes.teljesitve)
from diak join jelentkezes on jelentkezes.diakid = diak.id
group by jelentkezes.diakid
having count(jelentkezes.teljesitve = 0) > 1 or count(jelentkezes.ervenyes = 0) > 1 or count(jelentkezes.teljesitve = 0) + count(jelentkezes.ervenyes = 0) > 1