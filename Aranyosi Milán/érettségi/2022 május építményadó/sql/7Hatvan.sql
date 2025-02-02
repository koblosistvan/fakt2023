SELECT a.nev, h.vonalid
FROM allomas as a inner JOIN hely as h ON a.id = h.allomasid
WHERE h.vonalid IN (
    SELECT vonalid FROM hely WHERE allomasid = (SELECT id FROM allomas WHERE nev = 'Hatvan')
)
AND a.nev != 'Hatvan';
