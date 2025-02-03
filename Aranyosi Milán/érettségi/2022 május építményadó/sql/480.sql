SELECT a.nev, a.tipus, h.tav
FROM allomas as a inner JOIN hely as h ON a.id = h.allomasid
WHERE h.vonalid = '80' AND a.mukodo = TRUE
ORDER BY h.tav;
