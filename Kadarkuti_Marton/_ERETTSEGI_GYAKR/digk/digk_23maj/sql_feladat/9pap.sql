select distinct hang, cim
from szinkron inner join film on film.filmaz = szinkron.filmaz
where szinkron.filmaz in (
	select filmaz 
    from szinkron
    where hang like "%Pap Kati%"
)
and hang not like "%Pap Kati%"
order by cim, hang