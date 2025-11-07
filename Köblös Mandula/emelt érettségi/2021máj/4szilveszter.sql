SELECT l.helyezes, e.nev, d.cim
FROM eloadok as e INNER JOIN dalok as d on d.eloadoid = e.eloadoid
					INNER JOIN lista as l on l.dalid = d.dalid
WHERE l.ev = 2019 and l.helyezes <= 285
ORDER BY l.helyezes DESC
LIMIT 285;