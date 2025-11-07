SELECT DISTINCT nev
FROM diak
WHERE azon in (SELECT DISTINCT diakazon FROM jelentkezes) AND betujel = 'C' AND SELECT DISTINCT nev
FROM diak
WHERE azon in (SELECT DISTINCT diakazon FROM jelentkezes) AND betujel = 'C' AND evfolyam = 10
ORDER BY nevevfolyam = 10