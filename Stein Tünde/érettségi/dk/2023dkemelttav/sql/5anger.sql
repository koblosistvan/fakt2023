SELECT film.cim, film.eredeti, szinkron.szinesz, szinkron.szerep
FROM film JOIN szinkron ON szinkron.filmaz = film.filmaz
WHERE szinkron.hang = "Anger Zsolt";