SELECT a.nev, h.tav
FROM allomas as a INNER JOIN hely as h on a.id = h.allomasid
WHERE h.vonalid = 140 AND h.tav BETWEEN 90 AND 100;