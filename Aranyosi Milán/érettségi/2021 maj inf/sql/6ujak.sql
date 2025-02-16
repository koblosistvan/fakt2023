SELECT l.helyezes, e.nev, d.cim
FROM lista as l 
	INNER JOIN dalok as d on d.dalid = l.dalid
    INNER JOIN eloadok as e on e.eloadoid = d.eloadoid
WHERE l.ev=2019 And l.dalid not in (SELECT l.dalid
                           FROM lista as l
                           WHERE l.ev = 2018)
ORDER BY l.helyezes;