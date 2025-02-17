SELECT d.cim, e.nev
FROM lista as l 
	INNER JOIN dalok as d on d.dalid = l.dalid
    INNER JOIN eloadok as e on e.eloadoid = d.eloadoid
WHERE d.dalid in (SELECT l.dalid
                  FROM  lista as l 
                  WHERE l.helyezes = 1)
GROUP by l.dalid
HAVING count(*) = 21;