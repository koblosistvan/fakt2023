SELECT telepules.ut
FROM telepules
WHERE nev in (
    SELECT telepules.nev
    FROM telepules 
    WHERE telepules.ut = 'M6' ) AND 
 ut != 'M6';