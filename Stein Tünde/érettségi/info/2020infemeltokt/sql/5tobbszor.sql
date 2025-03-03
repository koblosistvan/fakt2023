SELECT diak.nev
FROM diak JOIN jelentkezes ON jelentkezes.diakid = diak.id
WHERE jelentkezes.elfogadva = -1 AND  jelentkezes.teljesitve = 0
GROUP BY diak.id
HAVING COUNT(jelentkezes.elfogadva) >= 2;