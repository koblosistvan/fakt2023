SELECT l.helyezes, e.nev, d.cim
FROM eloadok as e INNER JOIN dalok as d on d.eloadoid = e.eloadoid
					INNER JOIN lista as l on l.dalid = d.dalid
WHERE l.dalid IN(
    	SELECT lista.dalid
   	 	FROM lista
    	WHERE lista.ev = 2019)
    AND
    l.dalid NOT IN(
        SELECT lista.dalid
        FROM lista
        WHERE lista.ev = 2018)
ORDER BY l.helyezes;