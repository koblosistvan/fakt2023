SELECT DISTINCT evfolyam, betujel from diak
WHERE azon IN (
	SELECT DISTINCT diakazon FROM jelentkezes INNER JOIN szakkor on jelentkezes.szakazon = szakkor.azon
    WHERE mk LIKE "%matematika%"
)
ORDER BY evfolyam, betujel