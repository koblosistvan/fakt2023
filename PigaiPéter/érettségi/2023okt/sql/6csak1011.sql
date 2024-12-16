SELECT DISTINCT nev FROM szakkor
WHERE azon NOT IN (
	SELECT szakazon FROM jelentkezes INNER JOIN diak ON diak.azon = jelentkezes.diakazon
    WHERE evfolyam != 10 AND evfolyam != 11
)