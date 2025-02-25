SELECT a.nev, h.vonalid
FROM allomas as a INNER JOIN hely as h on a.id = h.allomasid
WHERE h.vonalid IN(
    SELECT hely.vonalid
    FROM hely INNER JOIN allomas on hely.allomasid = allomas.id 
    WHERE allomas.nev = 'Hatvan')
    AND a.nev != 'Hatvan';