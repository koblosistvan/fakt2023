SELECT l.helyezes, e.nev, d.cim
FROM lista as l 
	INNER JOIN dalok as d on d.dalid = l.dalid
    INNER JOIN eloadok as e on e.eloadoid = d.eloadoid
WHERE l.ev=2019 And l.helyezes<=285
ORDER BY l.helyezes;