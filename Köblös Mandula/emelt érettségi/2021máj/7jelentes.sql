SELECT l.ev, l.helyezes, e.nev, d.cim, d.megjelenes
FROM eloadok as e INNER JOIN dalok as d on d.eloadoid = e.eloadoid
					INNER JOIN lista as l on l.dalid = d.dalid
WHERE l.helyezes <= 10
ORDER BY l.ev;