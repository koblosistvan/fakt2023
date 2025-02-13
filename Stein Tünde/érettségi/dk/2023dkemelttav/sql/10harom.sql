SELECT szinkron.szinesz, szinkron.hang, COUNT(film.filmaz) as filmek_szama
from szinkron JOIN film ON film.filmaz = szinkron.filmaz
GROUP BY szinkron.szinesz, szinkron.hang
HAVING COUNT(film.filmaz) >= 3
ORDER BY filmek_szama DESC;