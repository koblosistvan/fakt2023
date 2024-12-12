SELECT DISTINCT szakkor.nev, diak.nev FROM jelentkezes INNER JOIN diak ON diak.azon = jelentkezes.diakazon INNER JOIN szakkor ON szakkor.azon = jelentkezes.szakazon
WHERE 
-- ugyanazok a szakkorok
szakazon IN ( 
	SELECT szakazon FROM jelentkezes INNER JOIN diak ON diak.azon = jelentkezes.diakazon
    WHERE diak.nev = "Beke Fanni"
) 
AND
-- ugyanaz az evfolyam
diak.evfolyam IN (
	SELECT evfolyam FROM jelentkezes INNER JOIN diak ON diak.azon = jelentkezes.diakazon
    WHERE diak.nev = "Beke Fanni"
)
AND
-- sajat maga nem szerepelhet
diak.nev != "Beke Fanni"