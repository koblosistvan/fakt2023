select distinct mafilmesek.hang, mafilmesek.ev
from (
	select hang, ev
    from szinkron inner join film on film.filmaz = szinkron.filmaz
    where studio = "Mafilm Audio Kft."
) as mafilmesek,
(
	select hang, ev
    from szinkron inner join film on film.filmaz = szinkron.filmaz
    where studio != "Mafilm Audio Kft."
) as nem_mafilmesek
where
mafilmesek.hang = nem_mafilmesek.hang and
mafilmesek.ev = nem_mafilmesek.ev
order by hang 