SELECT a.nev, COUNT(*) as vonalak
FROM allomas as a INNER JOIN hely as h on a.id = h.allomasid
GROUP BY h.allomasid
HAVING COUNT(*) >= 5
ORDER BY COUNT(*) DESC;