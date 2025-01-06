select cim, eredeti, szinesz, szerep
from film join szinkron on szinkron.filmaz = film.filmaz
where hang like "%Anger Zsolt%"