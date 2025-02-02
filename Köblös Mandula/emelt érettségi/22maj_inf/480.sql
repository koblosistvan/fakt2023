SELECT a.nev, a.tipus, h.tav
FROM allomas as a inner join hely as h on a.id = h.allomasid
				  INNER JOIN vonal as v on v.id = h.vonalid
WHERE v.mukodo AND v.id = 80
ORDER BY h.tav;