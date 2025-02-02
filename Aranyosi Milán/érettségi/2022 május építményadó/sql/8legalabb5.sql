SELECT a.nev, COUNT(h.vonalid) AS vonalak_szama
FROM allomas as a inner JOIN hely as h ON a.id = h.allomasid
GROUP BY a.nev
HAVING COUNT(h.vonalid) >= 5
ORDER BY vonalak_szama DESC;