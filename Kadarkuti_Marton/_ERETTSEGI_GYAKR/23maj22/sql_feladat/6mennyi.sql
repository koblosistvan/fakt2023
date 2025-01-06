select eredeti, cim, count(*) as szerepek_szama
from film inner join szinkron on film.filmaz = szinkron.filmaz
group by szinkron.filmaz