SELECT film.eredeti, film.cim, COUNT(szinkron.hang) as szereplok_szama
FROM film JOIN szinkron ON szinkron.filmaz = film.filmaz
GROUP BY film.filmaz;