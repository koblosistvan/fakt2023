SELECT szinkron.hang, film.cim
FROM szinkron JOIN film ON film.filmaz = szinkron.filmaz
WHERE film.cim in (
	SELECT film.cim
    FROM szinkron JOIN film ON film.filmaz = szinkron.filmaz
    WHERE szinkron.hang = "Pap Kati"
	)
AND szinkron.hang != "Pap Kati"
ORDER BY film.cim, szinkron.hang;